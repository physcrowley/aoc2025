from pathlib import Path
from typing import Tuple

def files(day: int, test: bool = False) -> Tuple[Path, Path] :
    day_name: str = "day" + str(day)
    data = Path(".") / day_name

    source = data / ("test.txt" if test else "input.txt")

    output_name = f'{"test_" if test else ""}output.txt'
    output = data / output_name

    return source, output

if __name__ == "__main__":
    print(files(2))
    print(files(3,True))