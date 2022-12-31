from typing import Iterable

from day04.parser import parse_input


def check_range_in_range(ranges):
    a, b = ranges[0]
    x, y = ranges[1]
    return 1 if a <= x and b >= y or a >= x and b <= y else 0


def solve(input: Iterable[str]) -> str:
    count = 0
    for line in input:
        ranges = parse_input(line)
        count += check_range_in_range(ranges)

    return count


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solve, __file__)
