from day05 import solution2
from day05.solution2 import solver


def test_solver():
    filled_stack_dict = {
        1: ["M"],
        2: ["C"],
        3: ["P", "Z", "N", "D"],
    }

    assert solver(filled_stack_dict) == "MCD"
