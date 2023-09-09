from typing import List, Tuple


def parse_input(input_list: List[str]) -> Tuple[List[str], List[str]]:
    stack_list, instructions_list = [], []
    mode = 0

    for line in input_list:
        if line == "":
            mode = 1
        elif mode == 0:
            stack_list.append(line)
        else:
            instructions_list.append(line)

    return stack_list, instructions_list
