from .marker_finder import find_marker_start


def solve(input):
    return find_marker_start(input, 4)


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solve, __file__)
