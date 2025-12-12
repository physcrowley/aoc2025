"""
Crée un nouveau fichier et dossier pour le numéro du jour
de l'activité voulu
"""
import sys
from pathlib import Path

usage: str = "Usage: `python new_day.py <day_no>`"

if len(sys.argv) != 2:
    print("Manque le jour")
    print(usage)
    sys.exit(1)

if not sys.argv[1].isdecimal():
    print("Le jour n'est pas un entier")
    print(usage)
    sys.exit(2)

day: int = int(sys.argv[1])

contents: str = f"""from files import files

day = {day}
test = True

source, output = files(day, test)

"""

# Créer le fichier
with open(f"day{day}.py", "w", encoding="utf-8") as f:
    f.write(contents)
# Créer le dossier
(Path(".") / f"day{day}").mkdir()