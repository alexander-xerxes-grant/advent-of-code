"""Doc."""

from typing import List

with open("input.txt") as f:
    lines = f.read().splitlines()


def box_checksum_calculator(box_ids: List) -> int:
    """Check for unique occurrences of pairs and triplets in box ids."""
    count_of_pairs = 0
    count_of_triplets = 0

    for id in box_ids:
        character_count_dict = {
            character: id.count(character) for character in id
        }
        if 2 in character_count_dict.values():
            count_of_pairs += 1
        if 3 in character_count_dict.values():
            count_of_triplets += 1

    return count_of_pairs * count_of_triplets


# print(count_characters(box_ids))
