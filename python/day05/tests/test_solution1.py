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
    solve,
)


class TestSolution:
    @pytest.fixture
    def filepath(self):
        return Path(__file__).parent.parent / "inputs" / "test_input.txt"

    def test_create_dict_of_stacks(self):
        stacks = ["    [D]    ", "[N] [C]    ", "[Z] [M] [P]", " 1   2   3 "]
        assert create_dict_of_stacks(stacks) == {1: [], 2: [], 3: []}

    def test_create_indexes(self):
        stacks = ["    [D]    ", "[N] [C]    ", "[Z] [M] [P]", " 1   2   3 "]
        assert create_indexes(stacks) == [1, 5, 9]

    def test_fill_stacks(self, filepath):
        stacks, _ = parse_input(filepath)
        stack_dict = {1: [], 2: [], 3: []}

        assert fill_stacks(stacks, stack_dict) == {
            1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"],
        }

    def test_parse_instructions_list(self, filepath):
        _, instructions = parse_input(filepath)
        assert parse_instructions_list(instructions) == [
            (1, 2, 1),
            (3, 1, 3),
            (2, 2, 1),
            (1, 1, 2),
        ]

    def test_move_crate(self):
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

    def test_crane(self, filepath):
        stacks, instructions = parse_input(filepath)

        assert crane(stacks, instructions) == {
            1: ["C"],
            2: ["M"],
            3: ["P", "D", "N", "Z"],
        }

    def test_solve(self):
        filled_stack_dict = {
            1: ["C"],
            2: ["M"],
            3: ["P", "D", "N", "Z"],
        }

        assert solve(filled_stack_dict) == "CMZ"
