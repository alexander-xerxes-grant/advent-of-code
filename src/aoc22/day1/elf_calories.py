"""
Take a list of integers representing calories carried by elves.

Elves are seperated by a new line.
Calculate the total calories carried by each elf, and return the max.
"""

import re
from typing import Generator

filename = "src/aoc22/day1/elf_calories_input.txt"


class CalculateCaloriesPerElf:
    """Calculate the maximum calorie intake for all elves."""

    def parse_input(self, filename: str):
        """Parse the input into a string.

        Parse the input file
        of each elf and returns the contents as a string.

        Args:
        filename: the name of the input file to be parsed.

        Returns:
        elves: a string containing the calorie intake of each elf.

        """
        with open(filename) as f:
            elves = f.read()
        return elves

    def split_elves(self, elves: str) -> Generator:
        """Split the string containing the calorie intake of each elf.

        Args:
        elves: a string containing the calorie intake of each elf.

        Returns:
        elves_split: a generator object containing the calorie intake
        of each elf as a list.

        """
        elves_split = re.findall(r"\d+(?:\n\d+)*", elves)
        return (elf.split("\n") for elf in elves_split)

    def calories_per_elf(self, elf) -> Generator:

        elf = [int(calorie) for calorie in elf]
        return elf

    def calculate(self) -> int:
        """Calculate the total calories carried by each elf.

        Args:
        self: the CalculateCaloriesPerElf instance calling the method.

        Returns:
        calories: a generator object containing the total calorie
        intake for each elf.

        """
        elves = self.parse_input(filename)
        for elf in self.split_elves(elves):
            calories = self.calories_per_elf(elf)
            yield sum(calories)


def main():
    """Calculate the maximum calorie intake for all elves."""
    elf_calculator = CalculateCaloriesPerElf()
    return max(elf_calculator.calculate())


if __name__ == "__main__":
    print(main())
