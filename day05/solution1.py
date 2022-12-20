from pathlib import Path
from typing import Iterable
import numpy as np
from utils.read import read_file_iter


def parse_lines(input):
    lines = input.strip().split("\n")
    return lines


# Use the following line instead if the input is a single line
# def solver(input: str) -> str:
# def solver(input: Iterable[str]) -> str:


# if __name__ == "__main__":
#     input_path = Path(__file__).parent / "input.txt"
#     input_iter = read_file_iter(input_path)

#     # Use the following line instead if the input is a single line
#     # print(solver(next(input_iter)), end="")
#     print(solver(input_iter), end="")
