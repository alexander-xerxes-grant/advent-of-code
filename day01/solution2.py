from typing import Iterable

from .parse_sum import sum_per_elf


def solver(input: Iterable[str]) -> int:
    elves = sorted(list(sum_per_elf(input)))
    return sum(elves[-3:])


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solver, __file__)
