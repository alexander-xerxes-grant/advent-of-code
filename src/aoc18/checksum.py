"""Doc."""
from typing import List


def open_file(filepath) -> List:
    """Open a file and return a list of the lines in the file."""
    try:
        with open(filepath) as f:
            box_ids = [line.strip() for line in f]
    except FileNotFoundError:
        raise FileNotFoundError("File not found")

    return box_ids


def char_frequency(box_id: str) -> dict:
    """Create a dictionary of the frequency of each character in a box id."""
    frequency_dict = {}
    # check if box_id is a string
    if not isinstance(box_id, str):
        raise TypeError("box_id must be a string")

    # check if the box id is empty
    if not box_id:
        raise ValueError("box_id must not be empty")

    # check if the box id contains spaces
    if " " in box_id:
        raise ValueError("box_id must not contain spaces")

    for char in box_id:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    return frequency_dict


def count_occurrences(frequency_dict: dict, id) -> tuple:
    """Count the number of pairs and triplets in a box id."""
    # Use a set to keep track of the box IDs that contain
    # a pair or a triplet.
    pairs = set()
    triplets = set()

    # Use the any() function to check if any elements
    # of the char_frequency_dict
    # match the target values of 2 and 3.
    # If so, add the box ID to the
    #  corresponding set.
    if any(x == 2 for x in frequency_dict.values()):
        pairs.add(id)
    if any(freq == 3 for freq in frequency_dict.values()):
        triplets.add(id)

    return pairs, triplets


def execute(filepath) -> int:
    """Execute the checksum algorithm."""
    count_pairs = 0
    count_triplets = 0

    box_ids = open_file(filepath)

    for id in box_ids:
        frequency_dict = char_frequency(id)
        pairs, triplets = count_occurrences(frequency_dict, id)
        count_pairs += len(pairs)
        count_triplets += len(triplets)

    return count_pairs * count_triplets


execute("src/aoc18/checksum_input.txt")
