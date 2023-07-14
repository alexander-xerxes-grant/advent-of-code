from pathlib import Path

import pytest
from day05.parser import parse_input


class TestParser:
    @pytest.fixture
    def filepath(self):
        return Path(__file__).parent.parent / "inputs" / "test_input.txt"

    def test_parse_input(self, filepath):

        assert parse_input(filepath) == (
            ["    [D]    ", "[N] [C]    ", "[Z] [M] [P]", " 1   2   3 "],
            [
                "move 1 from 2 to 1",
                "move 3 from 1 to 3",
                "move 2 from 2 to 1",
                "move 1 from 1 to 2",
            ],
        )
