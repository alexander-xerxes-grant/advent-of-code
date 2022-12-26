from pathlib import Path
from typing import Iterable

from utils.read import read_file_iter


# # Use the following line instead if the input is a single line
# # def solver(input: str) -> str:
# def solver(input: Iterable[str]) -> str:


def get_chunk(input, marker_length, i) -> str:
    return input[i : i + marker_length]


def check_unique(chunk: str, marker_length) -> bool:
    return len(chunk) and len(set(chunk)) == marker_length


def find_marker_start(input, marker_length) -> int:
    for i in range(0, len(input) - marker_length):
        if len(set(get_chunk(input, marker_length, i))) == marker_length:
            return i + marker_length


def solve(input):
    return find_marker_start(input, 4)


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solve, __file__)
