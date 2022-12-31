import pytest
from shared import get_input

from day01 import solution1
from day01.solution1 import solve


class TestSolution:
    @pytest.fixture
    def input(self):
        yield get_input(solution1.__file__, "tests/test_input.txt")

    def test_solver(self, input):
        solution = solve(input)

        assert solution == 24000
