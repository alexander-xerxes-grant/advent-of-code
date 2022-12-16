from pathlib import Path
from typing import Iterable, Tuple

from utils.read import read_file_iter


def parse_input(input: str):
    ranges = input.split(",")
    tuples = []
    for _range in ranges:
        for start, end in [_range.split("-")]:
            tuples.append((int(start), int(end)))
    return tuples


def construct_ranges(ranges: Iterable[Tuple[int, int]]) -> int:
    _range_1, _range_2 = [range(_range[0], _range[1]) for _range in ranges]
    return _range_1, _range_2


# Use the following line instead if the input is a single line
# def solver(input: str) -> str:
def solver(input: Iterable[str]) -> str:
    return "the answer"


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input.txt"
    input_iter = read_file_iter(input_path)

    # Use the following line instead if the input is a single line
    # print(solver(next(input_iter)), end="")
    print(solver(input_iter), end="")
