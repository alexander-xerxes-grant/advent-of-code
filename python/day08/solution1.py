#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def make_grid(input):
    return np.array([[int(i) for i in row] for row in input])


def trim_grid(input):
    grid = make_grid(input)
    return grid[1:-1, 1:-1]


def check_left(grid, current, row, column):
    return all(grid[row][x] < current for x in range(column))


def check_right(grid, current, row, column):
    return all(grid[row][x] < current for x in range(column + 1, len(grid)))


def check_up(grid, current, row, column):
    return all(grid[x][column] < current for x in range(row))


def check_down(grid, current, row, column):
    return all(grid[x][column] < current for x in range(row + 1, len(grid)))


def solve(puzzle_input):
    pass


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solve, __file__)
