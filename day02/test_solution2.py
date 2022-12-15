from day02.solution2 import player_move


# def test_calculate():
#     assert calculate("A Y") == 4


def test_player_move():
    assert player_move("A Y") == "X"
