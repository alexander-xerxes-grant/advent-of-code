from typing import Iterable
from .parser import parse_calories


def solve(input_list: Iterable[str]) -> int:
    list_of_elves = parse_calories(input_list)
    return sum(sorted([sum(elf) for elf in list_of_elves])[-3:])
    



if __name__ == "__main__":
    from shared import run_solver

    run_solver(solve, __file__)
