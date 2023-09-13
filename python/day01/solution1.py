from typing import Iterable

from .parser import parse_input


def solve(input_list):
    return parse_input(input_list)


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solve, __file__)
