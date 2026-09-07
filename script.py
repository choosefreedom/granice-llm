#!/usr/bin/env python3
"""
Jeden wspólny skrypt dla wszystkich pokoi — nie trzeba wchodzić do folderu roomN.
Uruchamiasz go z katalogu granice-llm (albo skądkolwiek), podajesz numer pokoju
(argumentem albo na pytanie), a skrypt sam ładuje Modelfile/questions z folderu
tego konkretnego pokoju i zapisuje wyniki w JEGO ai_results.md.

Każde pytanie z kolejki = osobne wywołanie `ollama run` = nowa konwersacja.
Po każdej odpowiedzi pytanie znika z kolejki, a wynik ląduje w ai_results.md.
"""

import os
import re
import subprocess
import sys
from datetime import datetime

# --- konfiguracja ---
BASE_MODEL = "gemma3:1b"      # model bazowy (ten, który masz pobrany)
MODEL = "gemma3-batch"        # nazwa modelu tworzonego z Modelfile
MODELFILE = "Modelfile"       # w środku ma być: FROM gemma3:1b
USE_MODELFILE = True          # False = odpal wprost gemma3:1b, bez `ollama create`
QUESTIONS = "questions"       # plik z pytaniami (zmieniasz go między przebiegami)
CONSUME = False               # True = pytanie znika z pliku po odpowiedzi
OUTPUT = "ai_results.md"
OUTPUT_MODE = "append"        # "append" = dopisuje | "overwrite" = kasuje stare | "timestamp" = nowy plik co przebieg
BACKUP = "questions.bak"      # kopia pełnej listy, robiona na starcie
TIMEOUT = 600                 # sekundy na jedno pytanie
INTERACTIVE_AFTER = True      # True = po kolejce oddaje terminal do `ollama run` (dopytywanie na żywo)
# --------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def dostepne_pokoje():
    """Lista numerów pokoi, dla których jest folder roomN obok tego skryptu."""
    numery = []
    for nazwa in os.listdir(SCRIPT_DIR):
        if nazwa.startswith("room") and nazwa[4:].isdigit():
            numery.append(int(nazwa[4:]))
    return sorted(numery)


def wybierz_pokoj():
    """Numer pokoju z argumentu (`python3 script.py 7`) albo z pytania na wejściu."""
    if len(sys.argv) > 1:
        numer = sys.argv[1].strip()
    else:
        print(f"==> dostępne pokoje: {', '.join(str(n) for n in dostepne_pokoje())}")
        numer = input("Numer pokoju: ").strip()

    if not numer.isdigit():
        sys.exit(f"BŁĄD: '{numer}' to nie jest numer pokoju")
    numer = str(int(numer))  # "01" -> "1", "007" -> "7"

    room_dir = os.path.join(SCRIPT_DIR, f"room{numer}")
    if not os.path.isdir(room_dir):
        sys.exit(f"BŁĄD: nie ma folderu {room_dir}")

    return numer, room_dir


ROOM, ROOM_DIR = wybierz_pokoj()
print(f"==> pokój {ROOM} -> {ROOM_DIR}")

# reszta ścieżek (Modelfile, questions, ai_results.md...) liczona jest już
# względem folderu WYBRANEGO pokoju
os.chdir(ROOM_DIR)

RUN_MODEL = MODEL if USE_MODELFILE else BASE_MODEL


def sh(cmd, stdin=None, timeout=None):
    """Odpowiednik odpalenia komendy w bashu."""
    return subprocess.run(cmd, input=stdin, capture_output=True, text=True, timeout=timeout)


def read_queue():
    """Zwraca listę pozostałych pytań (# = komentarz, pomijany)."""
    with open(QUESTIONS, encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip() and not l.startswith("#")]


def write_queue(remaining):
    """Nadpisuje plik pytań tym, co jeszcze zostało (atomowo, przez plik tymczasowy)."""
    tmp = QUESTIONS + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(remaining) + ("\n" if remaining else ""))
    os.replace(tmp, QUESTIONS)


def run_interactive_logged(cmd):
    """Odpala cmd tak, jakby ktoś sam wpisał je w terminalu (widać wszystko na
    żywo), a jednocześnie nagrywa całą widoczną sesję — to, co wpisaliście, i to,
    co odpowiedział model — i zwraca ją jako tekst do zapisania w ai_results.md.

    W przeciwieństwie do zwykłego `pty.spawn`, na starcie kopiuje rozmiar
    prawdziwego terminala do tego wewnętrznego (i dopasowuje go na bieżąco przy
    zmianie rozmiaru okna) — bez tego pełnoekranowy interfejs `ollama run`
    dostaje zerowy/losowy rozmiar i gubi się przy każdym wpisywanym znaku.

    Wymaga modułów `pty`/`termios`/`fcntl`, więc działa na Linuksie i macOS; na
    Windows ich nie ma, więc sesja się odbędzie normalnie, tylko bez nagrywania."""
    try:
        import fcntl
        import pty
        import select
        import signal
        import struct
        import termios
        import tty
    except ImportError:
        print("==> (Windows: brak pty/termios — sesja NIE zostanie zapisana do ai_results.md)")
        subprocess.run(cmd)
        return None

    def winsize():
        try:
            return fcntl.ioctl(sys.stdin.fileno(), termios.TIOCGWINSZ, b"\0" * 8)
        except OSError:
            return struct.pack("HHHH", 24, 80, 0, 0)  # fallback: 24 wiersze, 80 kolumn

    pid, master_fd = pty.fork()
    if pid == 0:  # proces potomny -> staje się `ollama run`
        os.execvp(cmd[0], cmd)
        os._exit(1)  # tylko gdyby execvp się nie powiodło

    def sync_winsize(*_a):
        try:
            fcntl.ioctl(master_fd, termios.TIOCSWINSZ, winsize())
        except OSError:
            pass

    sync_winsize()
    old_sigwinch = signal.signal(signal.SIGWINCH, sync_winsize)

    try:
        old_tty = termios.tcgetattr(sys.stdin.fileno())
        tty.setraw(sys.stdin.fileno())
        restore_tty = True
    except termios.error:
        restore_tty = False

    buf = bytearray()
    watch = [master_fd, sys.stdin.fileno()]
    try:
        while master_fd in watch:
            rfds, _, _ = select.select(watch, [], [])
            if master_fd in rfds:
                try:
                    data = os.read(master_fd, 1024)
                except OSError:
                    data = b""
                if not data:
                    break  # ollama zakończył działanie (/bye, Ctrl+D w środku, błąd...)
                buf.extend(data)
                os.write(sys.stdout.fileno(), data)
            if sys.stdin.fileno() in rfds:
                data = os.read(sys.stdin.fileno(), 1024)
                if not data:
                    # nasze stdin się zamknęło (rzadkie) — przestań go nasłuchiwać,
                    # ale czekaj dalej na to, co jeszcze odpowie ollama
                    watch.remove(sys.stdin.fileno())
                else:
                    os.write(master_fd, data)
    finally:
        if restore_tty:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSAFLUSH, old_tty)
        signal.signal(signal.SIGWINCH, old_sigwinch)
        os.close(master_fd)
        os.waitpid(pid, 0)

    text = buf.decode("utf-8", errors="replace")
    text = re.sub(r"\x1b\[[0-9;?]*[a-zA-Z]", "", text)  # usuń kody ANSI (kolory, kursor)
    return text.replace("\r\n", "\n").replace("\r", "\n")  # pty zwraca CRLF


# ollama create gemma3-batch -f Modelfile
if USE_MODELFILE:
    print(f"==> ollama create {MODEL} -f {MODELFILE}")
    res = sh(["ollama", "create", MODEL, "-f", MODELFILE])
    if res.returncode != 0:
        sys.exit(f"BŁĄD create: {res.stderr.strip()}")

queue = read_queue()
total = len(queue)
print(f"==> {total} pytań w kolejce ({QUESTIONS})")

# kopia zapasowa listy — tylko gdy plik ma być zjadany
if CONSUME:
    with open(BACKUP, "w", encoding="utf-8") as f:
        f.write("\n".join(queue) + "\n")

# tryb zapisu wyników
if OUTPUT_MODE == "timestamp":
    base, ext = os.path.splitext(OUTPUT)
    out_path, mode = f"{base}_{datetime.now():%Y-%m-%d_%H%M}{ext}", "w"
elif OUTPUT_MODE == "overwrite":
    out_path, mode = OUTPUT, "w"
else:
    out_path, mode = OUTPUT, "a"
print(f"==> zapis do {out_path} (tryb: {OUTPUT_MODE})")

with open(out_path, mode, encoding="utf-8") as out:
    out.write(f"\n# {RUN_MODEL} — {datetime.now():%Y-%m-%d %H:%M}\n\n")
    out.flush()

    done = 0
    while queue:
        q = queue[0]
        done += 1
        print(f"[{done}/{total}] {q[:60]}")

        # echo "pytanie" | ollama run gemma3-batch
        try:
            res = sh(["ollama", "run", RUN_MODEL], stdin=q, timeout=TIMEOUT)
            answer = res.stdout.strip() if res.returncode == 0 else f"BŁĄD: {res.stderr.strip()}"
        except subprocess.TimeoutExpired:
            answer = f"BŁĄD: przekroczono {TIMEOUT}s"

        # od razu na ekran, zeby nie trzeba bylo otwierac pliku
        print(f"\n{'=' * 60}\nODP: {answer}\n{'=' * 60}\n")

        # 1. zapis odpowiedzi
        out.write(f"### {done}. {q}\n{answer}\n\n{'-' * 60}\n\n")
        out.flush()

        # 2. dopiero teraz pytanie znika z kolejki
        queue.pop(0)
        if CONSUME:
            write_queue(queue)

print(f"==> gotowe -> {out_path} ({total} pytań, model {RUN_MODEL})")

if INTERACTIVE_AFTER:
    # oddajemy terminal modelowi — możecie dopytać, zadać pytanie rozstrzygające itd.
    # koniec sesji: /bye albo Ctrl+D. Cała sesja ląduje na końcu ai_results.md.
    print(f"\n==> otwieram interaktywną sesję z {RUN_MODEL} (wyjście: /bye albo Ctrl+D)\n")
    session = run_interactive_logged(["ollama", "run", RUN_MODEL])
    if session:
        with open(out_path, "a", encoding="utf-8") as out:
            out.write(f"\n## Sesja interaktywna — {datetime.now():%Y-%m-%d %H:%M}\n\n")
            out.write("```\n")
            out.write(session.strip() + "\n")
            out.write("```\n")
        print(f"==> zapisano sesję interaktywną -> {out_path}")
else:
    # ollama stop — koniec sesji, model out z pamięci
    print(f"==> ollama stop {RUN_MODEL}")
    sh(["ollama", "stop", RUN_MODEL])
