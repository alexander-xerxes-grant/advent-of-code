from typing import Iterable, Tuple

# X = "Lose"
# Y = "Draw"
# Z = "Win"


# A Y
# B X
# C Z --> 12

# instead of X, Y and Z encoding the moves, they encode the outcomes
# for example, if our opponent plays A (Rock), and the outcome is X (Lose), then
# we need to play C (Scissors) to lose. This means we need to play -1 (mod 3) of
# the opponent's move.


moves = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": -1,
    "Y": 0,
    "Z": 1,
}


# The points for each move: rock, paper, scissors respectively
scores = [1, 2, 3]


def parse_input(input: str) -> Tuple[int, int]:
    opponent, outcome = [moves[i] for i in input.split()]
    return (opponent, outcome)


def calculate_score(opponent: int, outcome: int) -> int:
    score = 0
    score += (outcome + 1) * 3
    score += scores[(outcome + opponent) % 3]
    return score


def solve(input: Iterable[str]) -> str:
    total_score = 0
    for line in input:
        opponent, player = parse_input(line)

        total_score += calculate_score(opponent, player)

    return total_score


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solve, __file__)
