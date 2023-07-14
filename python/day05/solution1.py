from pathlib import Path
from typing import Dict, List, Tuple

from day05.parser import parse_input


def create_dict_of_stacks(stacks: List[str]) -> Dict[int, List[str]]:
    return {int(digit): [] for digit in stacks[-1].replace(" ", "")}


def create_indexes(stacks: List[str]) -> List[int]:
    return [i for i, char in enumerate(stacks[-1]) if char != " "]


def fill_stacks(
    stacks: List[str], stack_dict: Dict[int, List[str]]
) -> Dict[int, List[str]]:
    indexes = create_indexes(stacks)

    for string in stacks[:-1]:
        stack_num = 1
        for i in indexes:
            if string[i] != " ":
                stack_dict[stack_num].insert(0, string[i])
            stack_num += 1

    return stack_dict


def parse_instructions_list(
    instructions_list: List[str],
) -> List[Tuple[int, int, int]]:
    parsed_instructions_list = []

    for instruction in instructions_list:
        words = instruction.split()
        crate_num = int(words[1])
        from_stack = int(words[3])
        to_stack = int(words[5])
        parsed_instructions_list.append((crate_num, from_stack, to_stack))

    return parsed_instructions_list


def move_crate(instruction, filled_stack_dict):
    crate_num, from_stack, to_stack = instruction

    for _ in range(crate_num):
        removed_crate = filled_stack_dict[from_stack].pop()
        filled_stack_dict[to_stack].append(removed_crate)

    return filled_stack_dict


def crane(stacks, instructions_list):
    instructions_list = parse_instructions_list(instructions_list)
    stack_dict = create_dict_of_stacks(stacks)
    filled_stack_dict = fill_stacks(stacks, stack_dict)

    for instruction in instructions_list:

        filled_stack_dict = move_crate(instruction, filled_stack_dict)

    return filled_stack_dict


def solve(filepath):
    stacks, instructions_list = parse_input(filepath)
    filled_stack_dict = crane(stacks, instructions_list)
    return "".join(stack[-1] for stack in filled_stack_dict.values())

if __name__ == "__main__":
    from shared import run_solver

    run_solver(solve, __file__)

