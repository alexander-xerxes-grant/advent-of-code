from typing import List, Tuple


def parse_input(filepath: str) -> Tuple[List[str], List[str]]:
    with open(filepath) as f:
        stack_list, instructions_list = (
            i.splitlines() for i in f.read().strip("\n").split("\n\n")
        )

    return stack_list, instructions_list
