from pathlib import Path
from typing import Iterable, List, Tuple

from utils.read import read_file_iter

# To solve this you need to parse the strategy guide to determine what the actions of each player
# will be. Then for each round you will need to determine the outcome (W, L, or D) of the round.
# next, calculate the score for each round. The score for a round is the sum of the score
# for each actions (1 for Rock, 2 for Paper, 3 for Scissors) and the score for the outcomes
# (0 for loss, 3 for draw, and 6 for win).
# Finally, add up the scores for all of the rounds to get the final score.

# 1. Parse the strategy guide to determine the actions for each player in each round.
# 2. Determine the outcome of each round (win, loss, or draw) based on the actions of both players.
# 3. Calculate the score for each round by adding the score for the action and the score for the outcome.
# 4. Add up the scores for all of the rounds to get the final score.

moves = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

move_outcomes = {
    4: "Win",
    2: "Draw",
    3: "Loss",
}


outcomes = {
    "Win": 6,
    "Draw": 3,
    "Loss": 0,
}


def strip_n_replace(input: Iterable[str]) -> List[Tuple[str, str]]:
    split_input = input.split(",")
    return [x.replace(" ", "") for x in split_input]


def parse_input(input: Iterable[str]) -> List[Tuple[int, int]]:
    return [(x[0], x[1]) for x in strip_n_replace(input)]


# Use the following line instead if the input is a single line
# def solver(input: str) -> str:
def solver(input: Iterable[str]) -> str:
    return "the answer"


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input.txt"
    input_iter = read_file_iter(input_path)

    # Use the following line instead if the input is a single line
    # print(solver(next(input_iter)), end="")
    print(solver(input_iter), end="")
