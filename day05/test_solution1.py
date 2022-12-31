from pathlib import Path

import pytest

from day05.solution1 import (
    crane,
    create_dict_of_stacks,
    create_indexes,
    fill_stacks,
    move_crate,
    parse_input,
    parse_instructions_list,
    solver,
)


def test_parse_input():
    filepath = Path(__file__).parent / "test_input.txt"

    assert parse_input(filepath) == (
        ["    [D]    ", "[N] [C]    ", "[Z] [M] [P]", " 1   2   3 "],
        [
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2",
        ],
    )


def test_create_dict_of_stacks():
    stacks = ["    [D]    ", "[N] [C]    ", "[Z] [M] [P]", " 1   2   3 "]
    assert create_dict_of_stacks(stacks) == {1: [], 2: [], 3: []}


def test_create_indexes():
    stacks = ["    [D]    ", "[N] [C]    ", "[Z] [M] [P]", " 1   2   3 "]
    assert create_indexes(stacks) == [1, 5, 9]


def test_fill_stacks():
    filepath = Path(__file__).parent / "test_input.txt"
    stacks, _ = parse_input(filepath)
    stack_dict = {1: [], 2: [], 3: []}

    assert fill_stacks(stacks, stack_dict) == {
        1: ["Z", "N"],
        2: ["M", "C", "D"],
        3: ["P"],
    }


def test_parse_instructions_list():
    filepath = Path(__file__).parent / "test_input.txt"
    _, instructions = parse_input(filepath)
    assert parse_instructions_list(instructions) == [
        (1, 2, 1),
        (3, 1, 3),
        (2, 2, 1),
        (1, 1, 2),
    ]


def test_move_crate():
    instruction = (1, 2, 1)
    filled_stack_dict = {
        1: ["C"],
        2: ["M"],
        3: ["P", "D", "N", "Z"],
    }

    assert move_crate(instruction, filled_stack_dict) == {
        1: ["C", "M"],
        2: [],
        3: ["P", "D", "N", "Z"],
    }


def test_crane():
    filepath = Path(__file__).parent / "test_input.txt"
    stacks, instructions = parse_input(filepath)

    assert crane(stacks, instructions) == {
        1: ["C"],
        2: ["M"],
        3: ["P", "D", "N", "Z"],
    }


def test_solver():
    filled_stack_dict = {
        1: ["C"],
        2: ["M"],
        3: ["P", "D", "N", "Z"],
    }

    assert solver(filled_stack_dict) == "CMZ"
