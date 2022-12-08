from unittest import mock

import pytest

from src.aoc22.day1.elf_calories import CalculateCaloriesPerElf


class TestCalculateCaloriesPerElf:
    @pytest.fixture
    def elf_calculator(self):
        return CalculateCaloriesPerElf()

    def test_parse_input_returns_expected_string(self, elf_calculator):

        expected_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

        input_text = elf_calculator.parse_input(
            "tests/unit_tests/aoc22/test_day1/elf_calories_example.txt"
        )

        assert input_text == expected_input

    def test_parse_input_called_with_valid_filepath(self, elf_calculator):

        expected_filename = "tests/unit_tests/elf_calories_example.txt"
        parse_input_mock = mock.Mock()
        elf_calculator.parse_input = parse_input_mock

        elf_calculator.parse_input(expected_filename)

        assert elf_calculator.parse_input.called_once_with(expected_filename)

    def test_split_elves_splits_when_only_one_elf(self, elf_calculator):

        elves = "123\n"
        split_elves = elf_calculator.split_elves(elves)

        assert list(split_elves) == [["123"]]

    def test_split_elves_splits_when_multiple_elves(self, elf_calculator):

        elves = "123\n456\n789\n"
        split_elves = elf_calculator.split_elves(elves)

        assert list(split_elves) == [["123", "456", "789"]]

    def test_split_elves_splits_when_multiple_elves_with_empty_lines(
        self, elf_calculator
    ):

        elves = "123\n\n456\n789\n"
        split_elves = elf_calculator.split_elves(elves)

        assert list(split_elves) == [["123"], ["456", "789"]]

    # def test_calculate_calories_per_elf(self, elf_calculator):

    #     # elves = "3\n5\n7\n"
    #     # expected_max_calories = 15
    #     # assert (
    #     #     list(elf_calculator.calculate_calories_per_elf(elves))
    #     #     == expected_max_calories
    #     # )

    #     # Test the case where the input contains no elves.
    #     elves = ""
    #     split_elves =
    #     expected_max_calories = 0
    #     assert (
    #         list(elf_calculator.calculate_calories_per_elf())
    #         == expected_max_calories
    #     )
