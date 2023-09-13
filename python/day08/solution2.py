# !/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

from .solution1 import make_grid


def check_scenic_score_left(
    grid: List[List[int]], current: int, row: int, column: int
) -> int:
    count = 0
    for x in range(column - 1, -1, -1):
        count += 1
        if grid[row][x] >= current:
            break

    return count


def check_scenic_score_right(
    grid: List[List[int]], current: int, row: int, column: int
) -> int:
    count = 0
    for x in range(column + 1, len(grid[row])):
        count += 1
        if grid[row][x] >= current:
            break

    return count


def check_scenic_score_up(
    grid: List[List[int]], current: int, row: int, column: int
) -> int:
    count = 0
    for x in range(row - 1, -1, -1):
        count += 1
        if grid[x][column] >= current:
            break

    return count


def check_scenic_score_down(
    grid: List[List[int]], current: int, row: int, column: int
) -> int:
    count = 0
    for x in range(row + 1, len(grid)):
        count += 1
        if grid[x][column] >= current:
            break

    return count


def check_scenic_score(
    grid: List[List[int]], current: int, row: int, column: int
) -> int:
    left = check_scenic_score_left(grid, current, row, column)
    right = check_scenic_score_right(grid, current, row, column)
    up = check_scenic_score_up(grid, current, row, column)
    down = check_scenic_score_down(grid, current, row, column)

    return max(0, left * right * up * down)


def solve(puzzle_input) -> int:
    grid = make_grid(puzzle_input)
    max = 0

    for row in range(len(grid[0])):
        for column in range(len(grid)):
            current = grid[row][column]
            score = check_scenic_score(grid, current, row, column)
            if score > max:
                max = score
    return max


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solve, __file__)
