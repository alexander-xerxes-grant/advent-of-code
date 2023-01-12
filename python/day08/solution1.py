#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def make_grid(input):
    return np.array([[int(i) for i in row] for row in input])


def check_left(grid, current, row, column):
    return all(grid[row][x] < current for x in range(column))


def check_right(grid, current, row, column):
    return all(grid[row][x] < current for x in range(column + 1, len(grid)))


def check_up(grid, current, row, column):
    return all(grid[x][column] < current for x in range(row))


def check_down(grid, current, row, column):
    return all(grid[x][column] < current for x in range(row + 1, len(grid)))


def check_visibility(grid, current, row, column):
    count = 0
    if (
        check_up(grid, current, row, column)
        or check_down(grid, current, row, column)
        or check_left(grid, current, row, column)
        or check_right(grid, current, row, column)
    ):
        count += 1
    return count


def count_outside_trees(grid):
    return 2 * (len(grid) + len(grid[0])) - 4


def solve(puzzle_input):
    grid = make_grid(puzzle_input)
    count = 0
    outer_trees = count_outside_trees(grid)
    for row in range(1, len(grid) - 1):
        for column in range(1, len(grid) - 1):
            current = grid[row][column]
            count += check_visibility(grid, current, row, column)
    return count + outer_trees


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solve, __file__)
