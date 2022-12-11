from pathlib import Path
from typing import Iterable, List, Tuple

from utils.read import read_file_iter

# To solve this you need to parse the strategy guide to determine what the actions of each player
# will be. Then for each round you will need to determine the outcome (W, L, or D) of the round.
# next, calculate the score for each round. The score for a round is the sum of the score
# for each actions (1 for Rock, 2 for Paper, 3 for Scissors) and the score for the outcomes
# (0 for loss, 3 for draw, and 6 for win).
# Finally, add up the scores for all of the rounds to get the final score.

# I decided to change the moves dict values to 0, 1 and 2 for rock, paper,
# and scissors respectively. This way I can use the modulus operator to
# determine the outcome of the round.
# if the player wins, the outcome will be 1,
# if it is a draw, the outcome will be 0
# if the player loses, the outcome will be 2


moves = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}

# The points for each move: rock, paper, scissors respectively
scores = [1, 2, 3]


def parse_input(input: str) -> List[Tuple[str, str]]:
    moves_list = [tuple(i.split()) for i in input.split(", ")]
    return moves_list


def map_moves(moves_list: List[Tuple[str, str]]) -> List[Tuple[int, int]]:
    moves_list = parse_input(moves_list)
    return [(moves[opp], moves[plr]) for (opp, plr) in moves_list]
