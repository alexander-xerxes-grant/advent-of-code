from day02.solution2 import parse_input, calculate_score


# def test_calculate():
#     assert calculate("A Y") == 4


# def test_player_move():
#     assert player_move("A Y") == "X"
#     assert player_move("B X") == "X"
#     assert player_move("C Z") == "X"


def test_parse_input():
    assert parse_input("A Y") == (0, 0)
    assert parse_input("B X") == (1, -1)
    assert parse_input("C Z") == (2, 1)


def test_calculate_score():
    assert calculate_score(0, 0) == 4
    assert calculate_score(1, -1) == 1
    assert calculate_score(2, 1) == 7
