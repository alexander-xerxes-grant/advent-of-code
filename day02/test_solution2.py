from day02.solution2 import parse_input


# def test_calculate():
#     assert calculate("A Y") == 4


# def test_player_move():
#     assert player_move("A Y") == "X"
#     assert player_move("B X") == "X"
#     assert player_move("C Z") == "X"


def test_parse_input():
    assert parse_input("A X") == (0, -1)
    assert parse_input("B Y") == (1, 0)
    assert parse_input("C Z") == (2, 1)
