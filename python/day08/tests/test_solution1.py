#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy.testing as npt
import pytest
from shared import get_input

from .. import solution1
from ..solution1 import (
    check_down,
    check_left,
    check_right,
    check_up,
    check_visibility,
    make_grid,
    pad_grid,
    solve,
    trim_grid,
)


class TestSolution:
    @pytest.fixture
    def puzzle_input(self):
        yield get_input(solution1.__file__, "test_input.txt")

    def test_make_grid(self, puzzle_input):
        npt.assert_equal(
            make_grid(puzzle_input),
            [
                [3, 0, 3, 7, 3],
                [2, 5, 5, 1, 2],
                [6, 5, 3, 3, 2],
                [3, 3, 5, 4, 9],
                [3, 5, 3, 9, 0],
            ],
        )

    def test_check_left(self):
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
        assert check_left(grid, current, row, column) is True
        assert check_left(grid, current, 3, column) is False

    def test_check_right(self):
        grid = [
            [9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9],
            [9, 9, 3, 1, 1],
            [9, 9, 1, 9, 9],
            [9, 9, 9, 9, 9],
        ]
        row = 2
        column = 2
        current = grid[row][column]
        assert check_right(grid, current, row, column) is True
        assert check_right(grid, current, 3, column) is False

    def test_check_up(self):
        grid = [
            [9, 9, 1, 9, 9],
            [9, 9, 1, 9, 9],
            [9, 9, 3, 1, 9],
            [9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9],
        ]
        row = 2
        column = 2
        current = grid[row][column]
        assert check_up(grid, current, row, column) is True
        assert check_up(grid, current, 3, column) is False

    def test_check_down(self):
        grid = [
            [9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9],
            [9, 9, 3, 1, 9],
            [9, 9, 1, 9, 9],
            [9, 9, 1, 9, 9],
        ]
        row = 2
        column = 2
        current = grid[row][column]
        assert check_down(grid, current, row, column) is True
        assert check_down(grid, current, 1, column) is False

    def test_check_visibility(self):
        grid = [
            [9, 9, 1, 9, 9],
            [9, 9, 1, 9, 9],
            [1, 1, 3, 1, 1],
            [9, 9, 1, 9, 9],
            [9, 9, 1, 9, 9],
        ]
        row = 2
        column = 2
        current = grid[row][column]
        assert check_visibility(grid, current, row, column) == 1

    def test_solve(self, puzzle_input):

        solution = solve(puzzle_input)

        assert solution == 21
