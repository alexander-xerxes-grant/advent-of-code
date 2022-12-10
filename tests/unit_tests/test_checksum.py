"""
    abcdef contains no letters that appear exactly two or three times.
    bababc contains two a and three b, so it counts for both.
    abbcde contains two b, but no letter appears exactly three times.
    abcccd contains three c, but no letter appears exactly two times.
    aabcdd contains two a and two d, but it only counts once.
    abcdee contains two e.
    ababab contains three a and three b, but it only counts once.
"""


# from unittest.mock import call, patch

import pytest

from src.aoc18.checksum import char_frequency, count_occurrences, open_file


def test_open_file():
    filepath = "tests/unit_tests/box_ids.txt"
    box_ids = open_file(filepath)
    assert box_ids == [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab",
    ]

    # Test with a file that does not exists
    filepath = "does_not_exist.txt"
    with pytest.raises(FileNotFoundError):
        open_file(filepath)

    # Test with an empty file
    filepath = "tests/unit_tests/empty.txt"
    with open(filepath, "w") as f:
        f.write("")
    box_ids = open_file(filepath)
    assert box_ids == []


def test_char_frequency():

    # Test with a valid box ID
    box_id = "abcdef"
    frequency_dict = char_frequency(box_id)
    assert frequency_dict == {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1}

    # Test with a box ID that contains a repeated characters
    box_id = "aabbcc"
    frequency_dict = char_frequency(box_id)
    assert frequency_dict == {"a": 2, "b": 2, "c": 2}

    # Test with a box ID that contains all the same characters
    box_id = "aaaaaa"
    frequency_dict = char_frequency(box_id)
    assert frequency_dict == {"a": 6}

    # Test with a box ID that contains no characters
    box_id = ""
    with pytest.raises(ValueError):
        char_frequency(box_id)

    # Test with a box ID that contains spaces
    box_id = "a b c"
    with pytest.raises(ValueError):
        char_frequency(box_id)

    # Test with a box ID that is not a string
    box_id = 123
    with pytest.raises(TypeError):
        char_frequency(box_id)


def test_char_frequency_raises_type_error():
    with pytest.raises(TypeError):
        char_frequency(123)

    with pytest.raises(TypeError):
        char_frequency(["a", "b", "c"])


def test_count_occurrences():

    # Test with a box ID that contains a pair
    frequency_dict = {"a": 2, "b": 1, "c": 1}
    id = "abac"
    pairs, triplets = count_occurrences(frequency_dict, id)

    assert pairs == {"abac"}
    assert triplets == set()

    # Test with a box ID that contains a triplet
    frequency_dict = {"a": 3, "b": 1}
    id = "aaab"
    pairs, triplets = count_occurrences(frequency_dict, id)

    assert pairs == set()
    assert triplets == {"aaab"}

    # Test with a box ID that contains a pair and a triplet
    frequency_dict = {"a": 2, "b": 3}
    id = "aabbb"
    pairs, triplets = count_occurrences(frequency_dict, id)

    assert pairs == {"aabbb"}
    assert triplets == {"aabbb"}

    # Test with a box ID that contains no pairs or triplets
    frequency_dict = {"a": 1, "b": 1, "c": 1}
    id = "abc"
    pairs, triplets = count_occurrences(frequency_dict, id)

    assert pairs == set()
    assert triplets == set()


# @patch("src.checksum.open_file")
# @patch("src.checksum.char_frequency")
# @patch("src.checksum.count_occurrences")
# def test_execute(mock_count_occurrences, mock_char_frequency,
# mock_open_file):

#     mock_open_file.return_value = [
#         "abcdef",
#         "bababc",
#         "abbcde",
#         "abcccd",
#         "aabcdd",
#         "abcdee",
#         "ababab",
#     ]

#     mock_char_frequency.return_value = {"a": 2, "b": 2, "c": 2}

#     mock_count_occurrences.return_value = {(2, 3), "aabbcc"}

#     assert execute("tests/unit_tests/box_ids.txt") == 12
