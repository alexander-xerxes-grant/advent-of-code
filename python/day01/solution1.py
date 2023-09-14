from .parser import parse_calories


def solve(input_list):
    list_of_elves = parse_calories(input_list)
    return max([sum(elf) for elf in list_of_elves])


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solve, __file__)
