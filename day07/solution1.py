import re
from typing import Iterable


def check_command(input):
    res = []
    input = str(input)

    pattern = re.compile(r"^\$.+", flags=re.MULTILINE)

    matches = pattern.finditer(input)

    for match in matches:
        res.append(match.group())

    return res


# Use the following line instead if the input is a single line
# def solver(input: str) -> str:
def solve(input: Iterable[str]) -> str:
    return "the answer"


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solve, __file__)
