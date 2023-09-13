#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from shared import get_input

from .. import solution2
from ..solution2 import (
    check_scenic_score,
    check_scenic_score_down,
    check_scenic_score_left,
    check_scenic_score_right,
    check_scenic_score_up,
)


class TestSolution:
    @pytest.fixture
    def puzzle_input(self):
        yield get_input(solution2.__file__, "test_input.txt")

    def test_check_scenic_score_left(self):
        grid = [
            [9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9],
            [1, 1, 3, 9, 9],
            [9, 9, 1, 9, 9],
            [9, 9, 9, 9, 9],
        ]
        row = 2
        column = 2
        current = grid[row][column]
        assert check_scenic_score_left(grid, current, row, column) == 2

    def test_check_scenic_score_right(self):
        grid = [
            [9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9],
            [9, 9, 3, 1, 1],
            [9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9],
        ]
        row = 2
        column = 2
        current = grid[row][column]

        assert check_scenic_score_right(grid, current, row, column) == 2

    def test_check_scenic_score_up(self):
        grid = [
            [9, 9, 3, 9, 9],
            [9, 9, 3, 9, 9],
            [1, 2, 3, 1, 1],
            [9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9],
        ]
        row = 3
        column = 2
        current = grid[row][column]

        assert check_scenic_score_up(grid, current, 4, 2) == 1
        assert check_scenic_score_up(grid, current, 3, 2) == 3

    def test_check_scenic_score_down(self):
        grid = [
            [9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9],
            [1, 1, 3, 9, 9],
            [9, 9, 2, 9, 9],
            [9, 9, 6, 9, 9],
        ]
        row = 1
        column = 2
        current = grid[row][column]

        assert check_scenic_score_down(grid, current, row, column) == 3

    def test_check_scenic_score(self):
        grid = [
            [1, 9, 9, 9, 9],
            [9, 9, 9, 9, 9],
            [1, 1, 3, 9, 9],
            [9, 9, 1, 9, 9],
            [9, 9, 9, 9, 9],
        ]
        row = 2
        column = 2
        current = grid[row][column]
        assert check_scenic_score(grid, current, row, column) == 4

        row = 1
        column = 2
        current = grid[row][column]
        assert check_scenic_score(grid, current, row, column) == 3

    def test_solve(self, puzzle_input):

        assert solution2.solve(puzzle_input) == 8
