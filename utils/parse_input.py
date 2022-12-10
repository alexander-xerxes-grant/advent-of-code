"""This function parses the input for the AOC problems."""

from typing import List


def parse_input(filename: str) -> List:
    """Parse the input file."""
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines
