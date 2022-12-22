from pathlib import Path
from typing import Iterable


filepath = Path(__file__).parent / "test_input.txt"


def parse_input(filepath):
    with open(filepath) as f:
        stack_strings, instructions = (
            i.splitlines() for i in f.read().strip("\n").split("\n\n")
        )
    return stack_strings, instructions


def create_dict_of_stacks(stacks):
    stack_dict = {int(digit): [] for digit in stacks[-1].replace(" ", "")}
    return stack_dict


def create_indexes(stacks):
    indexes = [i for i, char in enumerate(stacks[-1]) if char != " "]
    return indexes


def fill_stacks(stacks, stack_dict):
    indexes = create_indexes(stacks)

    for string in stacks[:-1]:
        stack_num = 1
        for i in indexes:
            if string[i] != " ":
                stack_dict[stack_num].insert(0, string[i])
            stack_num += 1
    return stack_dict


def parse_instructions(instructions):
    parsed_instructions = []
    for instruction in instructions:
        words = instruction.split()
        crate_num = int(words[1])
        from_stack = int(words[3])
        to_stack = int(words[5])
        parsed_instructions.append((crate_num, from_stack, to_stack))
    return parsed_instructions


# stacks, instructions = parse_stacks_instructions(read_file(filepath))
# stack_dict = create_dict_of_stacks(stacks)
# indexes = create_indexes(stacks)
# # stack_dict = fill_stacks(stacks, stack_dict)``

# print("\nStacks", stacks)
# print("\nInstructions", instructions)
# print("\nIndexes", indexes)
# print("\nStack Dict", stack_dict)

# Use the following line instead if the input is a single line
# def solver(input: str) -> str:
# def solver(input: Iterable[str]) -> str:


# if __name__ == "__main__":
#     input_path = Path(__file__).parent / "input.txt"
#     input_iter = read_file_iter(input_path)

#     # Use the following line instead if the input is a single line
#     # print(solver(next(input_iter)), end="")
#     print(solver(input_iter), end="")
