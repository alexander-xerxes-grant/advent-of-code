"""Doc."""

from typing import List

with open("input.txt") as f:
    lines = f.read().splitlines()


def char_frequency(box_id):
    return {
        character: box_id.count(character) for character in box_id
    }


def has_pair(char_counts):
    return 2 in char_counts.values()


def has_triplets(char_counts):
    return 3 in char_counts.values()


def box_checksum_calculator(box_ids: List) -> int:
    """Check for unique occurrences of pairs and triplets in box ids."""
    count_of_pairs = 0
    count_of_triplets = 0

    for id in box_ids:
        character_count_dict = char_frequency(id)

        if has_pair(character_count_dict):
            count_of_pairs += 1
        if has_triplets(character_count_dict):
            count_of_triplets += 1

    return count_of_pairs * count_of_triplets


# print(count_characters(box_ids))
