import pytest

from day04 import solution2
from day04.solution2 import check_range_overlaps, solve
from shared import get_input


class TestSolution:
    @pytest.fixture
    def input_list(self):
        yield get_input(solution2.__file__, "test_input.txt")

    def test_check_range_overlaps(self):
        assert check_range_overlaps([[2, 4], [6, 8]]) == 0
        assert check_range_overlaps([[2, 3], [0, 5]]) == 1
        assert check_range_overlaps([[10, 15], [9, 16]]) == 1
        assert check_range_overlaps([[1, 2], [2, 4]]) == 1
        assert check_range_overlaps([[2, 5], [3, 6]]) == 1
        assert check_range_overlaps([[9, 10], [3, 8]]) == 0

    def test_solver(self, input_list):
        solution = solve(input_list)

        assert solution == 4
