"""
Crée des chemins vers les fichiers d'entrée et de sortie
pour assurer une convention de nommage uniforme
"""

from pathlib import Path
from typing import Tuple

def files(day: int, test: bool = False) -> Tuple[Path, Path] :
    day_name: str = "day" + str(day)
    data = Path(".") / day_name

    source: Path = data / ("test.txt" if test else "input.txt")

    output_name: str = f'{"test_" if test else ""}output.txt'
    output: Path = data / output_name

    return source, output

# Tests de ce module
if __name__ == "__main__":
    print(files(2))
    print(files(3,True))