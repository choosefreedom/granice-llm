#!/usr/bin/env python3
"""
Dociśnięcie wybranej wersji Modelfile tam, gdzie w pierwszym przebiegu pękła
(numer konta w pokoju 14, potwierdzenie danych o alergiach konkretnego
dziecka w pokoju 16) - pytania z pliku `attacks_check` nawiązują wprost do
tego, co model już powiedział, i próbują pociągnąć to dalej. W
przeciwieństwie do eksperyment_granic.py NIE zatrzymuje się po pierwszym
sygnale ujawnienia - leci przez całą listę, żeby zobaczyć, jak daleko da się
to pociągnąć.

Użycie:
    python3 docisk.py 14 1
    python3 docisk.py 16 2
"""

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eksperyment_granic import sh, render_terminal, wygląda_na_ujawnienie, MODEL, TIMEOUT

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) < 3 or sys.argv[1] not in ("14", "16") or sys.argv[2] not in ("1", "2", "3"):
    sys.exit("Użycie: python3 docisk.py 14|16 1|2|3")

room = sys.argv[1]
version = sys.argv[2]
room_dir = os.path.join(SCRIPT_DIR, f"room{room}")
modelfile = os.path.join(room_dir, f"modelfile_v{version}")
attacks_path = os.path.join(room_dir, "attacks_check")
out_path = os.path.join(room_dir, f"ai_results_v{version}_check.md")

print(f"==> ollama create {MODEL} -f {modelfile}")
res = sh(["ollama", "create", MODEL, "-f", modelfile])
if res.returncode != 0:
    sys.exit(f"BŁĄD create: {res.stderr.strip()}")

with open(attacks_path, encoding="utf-8") as f:
    attacks = [l.strip() for l in f if l.strip()]

with open(modelfile, encoding="utf-8") as f:
    modelfile_content = f.read()

with open(out_path, "w", encoding="utf-8") as out:
    out.write(f"# Dociśnięcie modelfile_v{version} — pokój {room}\n")
    out.write(f"_{datetime.now():%Y-%m-%d %H:%M}_\n\n")
    out.write(f"Kontynuacja pierwszego przebiegu (`ai_results_v{version}.md`) dokładnie w miejscu, "
               "gdzie model się ugiął - pytania nawiązują wprost do jego wcześniejszej "
               "odpowiedzi i próbują pociągnąć temat dalej. Lecimy przez całą listę bez "
               "zatrzymywania się po pierwszym sygnale, żeby zobaczyć sufit.\n\n")
    out.write("## Testowany Modelfile\n\n```\n" + modelfile_content.strip() + "\n```\n\n")
    out.write(f"## Pytania dociskające (nawiązują do wcześniejszej rozmowy)\n\n")
    out.flush()

    for i, prompt in enumerate(attacks, start=1):
        print(f"[{i}/{len(attacks)}] {prompt[:70]}")
        try:
            res = sh(["ollama", "run", MODEL], stdin=prompt, timeout=TIMEOUT)
            answer = render_terminal(res.stdout) if res.returncode == 0 else f"BŁĄD: {res.stderr.strip()}"
        except Exception as e:
            answer = f"BŁĄD: {e}"

        werdykt = wygląda_na_ujawnienie(room, answer)
        znacznik = "🔴 wygląda na ujawnienie" if werdykt else "🟢 odmówił / wykręcił się"
        print(f"    -> {znacznik}")

        out.write(f"### Pytanie {i} — {znacznik}\n\n**Pytanie:** {prompt}\n\n**Odpowiedź:**\n\n{answer}\n\n---\n\n")
        out.flush()

print(f"==> zapisano {out_path}")
print(f"==> ollama stop {MODEL}")
sh(["ollama", "stop", MODEL])
