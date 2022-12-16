from pathlib import Path
from day02.solution2 import parse_input, calculate_score, solver_2
from utils.read import read_file_iter


def test_parse_input():
    assert parse_input("A Y") == (0, 0)
    assert parse_input("B X") == (1, -1)
    assert parse_input("C Z") == (2, 1)


def test_calculate_score():
    assert calculate_score(0, 0) == 4
    assert calculate_score(1, -1) == 1
    assert calculate_score(2, 1) == 7


def test_solver():
    input_path = Path(__file__).parent / "input.txt"
    input_iter = read_file_iter(input_path)

    assert solver_2(input_iter) == 12
