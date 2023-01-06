import pytest
from shared import get_input

from day04 import parser
from day04.parser import parse_input


class TestParser:
    @pytest.fixture
    def input_list(self):
        yield get_input(parser.__file__, "test_input.txt")

    def test_parse_input(self, input_list):
        assert parse_input(input_list[0]) == [[2, 4], [6, 8]]
        assert parse_input(input_list[1]) == [[2, 3], [4, 5]]
        assert parse_input(input_list[2]) == [[5, 7], [7, 9]]
