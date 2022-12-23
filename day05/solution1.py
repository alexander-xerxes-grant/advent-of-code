from pathlib import Path
from typing import Iterable


filepath = Path(__file__).parent / "input.txt"


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


def crane(stacks, instructions):
    instructions = parse_instructions(instructions)
    stack_dict = create_dict_of_stacks(stacks)
    filled_stack_dict = fill_stacks(stacks, stack_dict)

    for instruction in instructions:

        crate_num, from_stack, to_stack = instruction

        for crate in range(crate_num):
            removed_crate = filled_stack_dict[from_stack].pop()
            filled_stack_dict[to_stack].append(removed_crate)

    return filled_stack_dict


def solver(filled_stack_dict):

    return "".join(stack[-1] for stack in filled_stack_dict.values())


if __name__ == "__main__":
    stack_strings, instructions = parse_input(filepath)
    filled_stack_dict = crane(stack_strings, instructions)

    print(solver(filled_stack_dict))