from pathlib import Path
from typing import Iterable


from utils.read import read_file_iter

# X = "Lose"
# Y = "Draw"
# Z = "Win"


# A Y
# B X
# C Z --> 12

moves = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}

outcomes = {"X": 0, "Y": 3, "Z": 6}

# The points for each move: rock, paper, scissors respectively
scores = [1, 2, 3]


def player_move(opponent, outcome):
    pass


# def calculate(input):
#     opponent, outcome = [i for i in input.split()]
#     return outcomes[outcome] + scores[moves[opponent]]


# Use the following line instead if the input is a single line
# def solver(input: str) -> str:
def solver(input: Iterable[str]) -> str:
    return "the other answer"


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input.txt"
    input_iter = read_file_iter(input_path)

    # Use the following line instead if the input is a single line
    # print(solver(next(input_iter)), end="")
    print(solver(input_iter), end="")
