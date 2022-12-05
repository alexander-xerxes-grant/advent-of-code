"""
    abcdef contains no letters that appear exactly two or three times.
    bababc contains two a and three b, so it counts for both.
    abbcde contains two b, but no letter appears exactly three times.
    abcccd contains three c, but no letter appears exactly two times.
    aabcdd contains two a and two d, but it only counts once.
    abcdee contains two e.
    ababab contains three a and three b, but it only counts once.
"""

from src.checksum import box_checksum_calculator, char_frequency, has_pair, has_triplets


def test_input_is_list():
    expected_return = [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab",
    ]

    with open("tests/unit_tests/mock_input.txt") as f:
        lines = f.read().splitlines()

        assert lines == expected_return


def test_character_frequency():
    expected_return = {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1}

    assert char_frequency("abcdef") == expected_return


def test_has_pair():
    char_counts = {"a": 1, "b": 2, "c": 1, "d": 1, "e": 1}
    assert has_pair(char_counts) is True
    # To do: Add more tests, eg edge cases and False


def test_has_triplets():
    char_counts = {"a": 1, "b": 1, "c": 3, "d": 1}
    assert has_triplets(char_counts) is True
    # To do: Add more tests, eg edge cases and False


def test_box_checksum_calculator():
    mock_box_ids = [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab",
    ]

    assert box_checksum_calculator(mock_box_ids) == 12
