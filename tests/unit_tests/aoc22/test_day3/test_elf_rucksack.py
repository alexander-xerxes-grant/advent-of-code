import pytest

from src.aoc22.day3.elf_rucksack import parse_input, split_rucksacks


def test_parse_input_returns_expected_list():
    filepath = "tests/unit_tests/aoc22/test_day3/elf_rucksack_example.txt"

    expected_list = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]

    assert parse_input(filepath) == expected_list


def test_split_rucksacks():
    filepath = "tests/unit_tests/aoc22/test_day3/elf_rucksack_example.txt"
    rucksacks = parse_input(filepath)

    # Test function splits strings into two equal parts
    # Return double the number input
    # return a list
    # of strings
    # that are equal in length
    # What happens when a string has a length that isn't even
    compartments = split_rucksacks(rucksacks)

    assert split_rucksacks(rucksacks) == (len(rucksacks) * 2)
    assert len(compartments[0]) == len(rucksacks[0] / 2)


def test_split_rucksacks_returns_list():
    filepath = "tests/unit_tests/aoc22/test_day3/elf_rucksack_example.txt"
    rucksacks = parse_input(filepath)

    split_rucksacks(rucksacks).assertIsinstance(rucksacks, list)


def test_split_rucksacks_returns_list_of_string():
    filepath = "tests/unit_tests/aoc22/test_day3/elf_rucksack_example.txt"
    rucksacks = parse_input(filepath)

    compartments = split_rucksacks(rucksacks)

    # test all items in list are strings
    for compartment in compartments:
        assert isinstance(compartment, str)

    expected_list = [
        "vJrwpWtwJgW",
        "rhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
