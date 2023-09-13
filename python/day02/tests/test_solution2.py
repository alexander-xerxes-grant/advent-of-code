import pytest

from shared import get_input

from .. import solution2
from ..solution2 import calculate_score, parse_input, solve


class TestSolution:
    @pytest.fixture
    def input_text(self):
        yield get_input(solution2.__file__, "test_input.txt")

    def test_parse_input(self):
        assert parse_input("A Y") == (0, 0)
        assert parse_input("B X") == (1, -1)
        assert parse_input("C Z") == (2, 1)

    def test_calculate_score(self):
        assert calculate_score(0, 0) == 4
        assert calculate_score(1, -1) == 1
        assert calculate_score(2, 1) == 7

    def test_solver(self, input_text):
        solution = solve(input_text)

        assert solution == 12
