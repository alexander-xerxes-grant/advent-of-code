from typing import Iterable


def parse_input(input):
    current = []

    for line in input:
        if line:
            current.append(int(line))
        else:
            yield current
            current = []
    if current:
        yield current


def sum_per_elf(input):
    return (sum(elf) for elf in parse_input(input))


# Use the following line instead if the input is a single line
# def solver(input: str) -> str:
def solver(input: Iterable[str]) -> str:
    return max(sum_per_elf(input))


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solver, __file__)
