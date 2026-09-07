#!/usr/bin/env python3
"""
Uruchamia model Ollamy z Modelfile i zadaje mu pytania z pliku questions.
Każde pytanie = osobne wywołanie `ollama run` = nowa konwersacja.
Po każdej odpowiedzi pytanie znika z kolejki, a wynik ląduje w ai_results.txt.
"""

import os
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
OUTPUT = "ai_results.txt"
OUTPUT_MODE = "append"        # "append" = dopisuje | "overwrite" = kasuje stare | "timestamp" = nowy plik co przebieg
BACKUP = "questions.bak"      # kopia pełnej listy, robiona na starcie
TIMEOUT = 600                 # sekundy na jedno pytanie
# --------------------

RUN_MODEL = MODEL if USE_MODELFILE else BASE_MODEL

# wszystkie ścieżki liczone względem katalogu skryptu,
# więc można go odpalić z dowolnego miejsca w systemie
os.chdir(os.path.dirname(os.path.abspath(__file__)))


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

        # 1. zapis odpowiedzi
        out.write(f"### {done}. {q}\n{answer}\n\n{'-' * 60}\n\n")
        out.flush()

        # 2. dopiero teraz pytanie znika z kolejki
        queue.pop(0)
        if CONSUME:
            write_queue(queue)

# ollama stop — koniec sesji, model out z pamięci
print(f"==> ollama stop {RUN_MODEL}")
sh(["ollama", "stop", RUN_MODEL])
print(f"==> gotowe -> {out_path} ({total} pytań, model {RUN_MODEL})")
