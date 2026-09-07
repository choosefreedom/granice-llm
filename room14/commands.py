#!/usr/bin/env python3
"""
Uruchamia po kolei komendy z listy COMMANDS i zapisuje wynik do cmd_results.md.
Dla kazdej komendy zapisuje: jaka komenda zostala wywolana + jej wyjscie.
"""

import subprocess
from datetime import datetime

# --- komendy do uruchomienia (podmieniaj wedle potrzeby) ---
COMMANDS = [
#    "ls -la",
#    "whoami",
#    "id",
#    "pwd",
#    "cat /etc/passwd",
]


with open("commands", "r", encoding="utf-8") as file:
    for line in file:
        COMMANDS.append(line)
OUTPUT = "cmd_results.md"
# -----------------------------------------------------------

with open(OUTPUT, "w", encoding="utf-8") as out:
    out.write(f"# Wyniki komend — {datetime.now():%Y-%m-%d %H:%M}\n\n")

    for cmd in COMMANDS:
        print(f"==> {cmd}")

        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = res.stdout
        if res.stderr:
            output += res.stderr

        out.write(f"## `{cmd}`\n\n")
        out.write("```\n")
        out.write(output.rstrip() + "\n")
        out.write("```\n\n")
        out.flush()

print(f"==> gotowe -> {OUTPUT}")

# na koniec pokaz wynik
print("\n" + open(OUTPUT, encoding="utf-8").read())
