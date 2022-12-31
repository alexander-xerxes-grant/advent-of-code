import pytest
from shared import get_input

from .. import solution1
from ..solution1 import calculate_outcome, parse_input, solve


class TestSolution:
    @pytest.fixture
    def input_text(self):
        yield get_input(solution1.__file__, "tests/test_input.txt")

    def test_parse_input(self):
        assert parse_input("A X") == (0, 0)
        assert parse_input("B Y") == (1, 1)

    def test_calculate_outcome(self):
        assert calculate_outcome(0, 0) == 3
        assert calculate_outcome(0, 1) == 6
        assert calculate_outcome(0, 2) == 0

    def test_solve(self, input_text):
        solution = solve(input_text)

        assert solution == 15
