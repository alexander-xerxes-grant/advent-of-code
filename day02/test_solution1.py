from day02.solution1 import check_outcome, map_moves, parse_input


def test_parser():
    assert parse_input("A X, B Y, C Z") == [("A", "X"), ("B", "Y"), ("C", "Z")]
    assert parse_input("X Y, Z A") == [("X", "Y"), ("Z", "A")]


def test_map_moves():
    assert map_moves("A X, B Y, C Z") == [(0, 0), (1, 1), (2, 2)]
    assert map_moves("B Y, C X, C Z") == [(1, 1), (2, 0), (2, 2)]


def test_check_outcome():
    assert check_outcome(0, 0) == 3
    assert check_outcome(1, 1) == 3
    assert check_outcome(2, 2) == 3
    assert check_outcome(0, 1) == 0
    assert check_outcome(1, 2) == 0
    assert check_outcome(2, 0) == 0
    assert check_outcome(0, 2) == 6
    assert check_outcome(1, 0) == 6
    assert check_outcome(2, 1) == 6
