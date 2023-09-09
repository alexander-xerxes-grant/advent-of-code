from pathlib import Path

import pytest
from day01 import solution1
from day05.parser import parse_input
from shared import get_input


class TestParser:
    @pytest.fixture
    def input_list(self):
        yield get_input(solution1.__file__, "test_input.txt")

    def test_parse_input(self, input_list):
        assert parse_input(input_list) == (
            ["1000", "2000", "3000"],
            ["4000", "5000", "6000", "7000", "8000", "9000", "10000"],
        )
