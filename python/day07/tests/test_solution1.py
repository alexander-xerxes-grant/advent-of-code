import pytest

from day07.solution1 import solve
from shared import get_input


class TestSolution1:
    @pytest.fixture
    def puzzle_input(self):
        yield get_input(__file__, "test_input.txt")

    def test_solve(self, puzzle_input):
        pass
