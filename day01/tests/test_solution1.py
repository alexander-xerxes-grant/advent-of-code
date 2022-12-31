import pytest
from shared import get_input

from .. import solution1
from ..solution1 import solver


class TestSolution:
    @pytest.fixture
    def input(self):
        yield get_input(solution1.__file__, "tests/test_input.txt")

    def test_solver(self, input):
        solution = solver(input)

        assert solution == 24000
