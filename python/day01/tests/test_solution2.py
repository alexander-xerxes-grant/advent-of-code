import pytest

from day01 import solution2
from day01.solution2 import solve
from shared import get_input


class TestSolution:
    @pytest.fixture
    def input(self):
        yield get_input(solution2.__file__, "test_input.txt")

    def test_solve(self, input):
        solution = solve(input)

        assert solution == 45000
