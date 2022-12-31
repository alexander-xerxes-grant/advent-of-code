from pathlib import Path
from typing import Iterable, Tuple

from utils.read import read_file_iter


def parse_input(line: str):
    elves = line.split(",")
    ranges = [list(map(int, elf.split("-"))) for elf in elves]
    return ranges


def check_range_in_range(ranges):
    a, b = ranges[0]
    x, y = ranges[1]
    return 1 if a <= x and b >= y or a >= x and b <= y else 0


# Use the following line instead if the input is a single line
# def solver(input: str) -> str:
def solver(input: Iterable[str]) -> str:
    count = 0
    for line in input:
        ranges = parse_input(line)
        count += check_range_in_range(ranges)

    return count


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input.txt"
    input_iter = read_file_iter(input_path)

    # Use the following line instead if the input is a single line
    # print(solver(next(input_iter)), end="")
    print(solver(input_iter), end="")
