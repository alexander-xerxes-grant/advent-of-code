from pathlib import Path
from typing import Iterable

from utils.read import read_file_iter

from day01.solution1 import sum_per_elf


# Use the following line instead if the input is a single line
# def solver(input: str) -> str:
def solver(input: Iterable[str]) -> int:
    elves = sorted(list(sum_per_elf(input)))
    return sum(elves[-3:])


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input.txt"
    input_iter = read_file_iter(input_path)

    # Use the following line instead if the input is a single line
    # print(solver(next(input_iter)), end="")
    print(solver(input_iter), end="")
