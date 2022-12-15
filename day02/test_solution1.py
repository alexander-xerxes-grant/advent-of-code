from pathlib import Path
from day02.solution1 import parse_input, solver, calculate_outcome

from utils.read import read_file_iter


def test_parse_input():
    assert parse_input("A X") == (0, 0)
    assert parse_input("B Y") == (1, 1)


def test_calculate_outcome():
    assert calculate_outcome(0, 0) == 3
    assert calculate_outcome(0, 1) == 6
    assert calculate_outcome(0, 2) == 0


def test_solver():
    input_path = Path(__file__).parent / "test.txt"
    input_iter = read_file_iter(input_path)

    assert solver(input_iter) == 4
