# The points for each move: rock, paper, scissors respectively
scores = [1, 2, 3]

# Maps the opponent's move to a numeric value
opponent_moves = {
    "A": 0,  # rock
    "B": 1,  # paper
    "C": 2,  # scissors
}

# Maps the player's move to a numeric value
player_moves = {
    "X": 0,  # rock
    "Y": 1,  # paper
    "Z": 2,  # scissors
}

# Maps the outcome to a numeric value
outcomes = {
    "X": 0,  # loss
    "Y": 3,  # draw
    "Z": 6,  # win
}

# The strategy guide
strategy_guide = [
    ("A", "Y"),
    ("B", "X"),
    ("C", "Z"),
]

total_score = 0

for round in strategy_guide:
    # Get the opponent's move and the desired outcome
    opponent, outcome = round

    # Get the numeric value for the opponent's move
    opponent_move = opponent_moves[opponent]

    # Calculate the player's move based on the desired outcome
    player_move = (
        list(outcomes.keys()).index(outcome) - opponent_move + 3
    ) % 3

    # Use the player's move to index into the scores list
    score = scores[player_move]

    # Use the outcome to index into the outcomes dictionary
    score += outcomes[outcome]

    # Add the score for this round to the total score
    total_score += score

print(total_score)  # prints the total score
