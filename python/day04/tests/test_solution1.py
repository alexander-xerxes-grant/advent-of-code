import pytest
from shared import get_input

from day04 import solution1
from day04.solution1 import check_range_in_range, solve


class TestSolution:
    @pytest.fixture
    def input_list(self):
        yield get_input(solution1.__file__, "test_input.txt")

    def test_check_range_in_range(self):
        assert check_range_in_range([[2, 4], [6, 8]]) == 0
        assert check_range_in_range([[2, 3], [0, 5]]) == 1
        assert check_range_in_range([[10, 15], [9, 16]]) == 1

    def test_solver(self, input_list):
        solution = solve(input_list)

        assert solution == 2
