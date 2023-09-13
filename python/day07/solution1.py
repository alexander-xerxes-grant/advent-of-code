from collections import defaultdict
from itertools import accumulate
from typing import Iterable


# Use the following line instead if the input is a single line
# def solver(input: str) -> str:
def solve(input: Iterable[str]) -> str:
    dirs = defaultdict(int)

    for line in input:
        print(line.split())
        match line.split():
            case "$", "cd", "/":
                current = ["/"]
            case "$", "cd", "..":
                current.pop()
            case "$", "cd", x:
                current.append(x + "/")
            case "$", "ls":
                pass
            case "dir", _:
                pass
            case size, _:
                for p in accumulate(current):
                    dirs[p] += int(size)

    return sum(s for s in dirs.values() if s <= 100_000)


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solve, __file__)
