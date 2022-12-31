from day03.solution1 import (
    create_value_dict,
    find_common_letters,
    solver,
    split_items,
)
from day03.values_dict import create_value_dict


def test_create_value_dict():
    values_dict = create_value_dict()
    assert values_dict["A"] == 27
    assert values_dict["b"] == 2


def test_split_items():
    assert split_items("GGVG") == ["GG", "VG"]


def test_find_common_letters():
    assert find_common_letters(["GGGGGGGGG", "VGBBGG"]) == "G"
    assert find_common_letters(["ABCDEFG", ""]) == ""
    assert find_common_letters(["PmmdzqPrV", "vPwwTWBwg"]) == "P"
    assert find_common_letters(["jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"]) == "L"


def test_solver():

    input_list = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]

    assert solver(["vJrwpWtwJgWrhcsFMMfFFhFp"]) == 16
    assert solver(input_list) == 157
