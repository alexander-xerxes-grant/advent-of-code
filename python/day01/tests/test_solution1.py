import pytest
from day01 import solution1
from day01.solution1 import solve
from shared import get_input


class TestSolution:
    @pytest.fixture
    def input(self):
        yield get_input(solution1.__file__, "test_input.txt")

    def test_solver(self, input):
        pass
        solution = solve(input)

        # assert solution == 24000
