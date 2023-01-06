from typing import Iterable

from day04.parser import parse_input


def check_range_overlaps(ranges):
    a, b = ranges[0]
    x, y = ranges[1]
    return 1 if b >= x and a <= y else 0


def solve(input: Iterable[str]) -> str:
    count = 0
    for line in input:
        ranges = parse_input(line)
        count += check_range_overlaps(ranges)

    return count


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solve, __file__)
