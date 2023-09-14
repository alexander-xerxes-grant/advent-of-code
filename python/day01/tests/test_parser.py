import pytest

from day01 import solution1
from day01.parser import parse_calories, parse_item
from shared import get_input


class TestParser:
    @pytest.fixture
    def input_list(self):
        yield get_input(solution1.__file__, "test_input.txt")

    def test_parse_input_parses_calories(self, input_list):

        assert parse_calories(input_list) == [
            [1000, 2000, 3000],
            [4000],
            [5000, 6000],
            [7000, 8000, 9000],
            [10000],
        ]

    def test_parse_input_with_no_input(self):
        assert parse_calories([]) == [[]]

    def test_parse_input_consecutive_delimiters(self):
        input_list = ["1", "2", "", "", "4"]
        expected_output = [[1, 2], [4]]

        assert parse_calories(input_list) == expected_output

    def test_single_elf_single_item(self):
        assert parse_calories(["100"]) == [[100]]

    def test_single_elf_many_items(self):
        assert parse_calories(["1", "2", "3", "4", "5"]) == [[1, 2, 3, 4, 5]]

    def test_multiple_elves_single_item_each(self):
        assert parse_calories(["1", "", "2", "", "3"]) == [[1], [2], [3]]

    def test_parse_item_raises(self):
        with pytest.raises(ValueError):
            parse_item("abc")
