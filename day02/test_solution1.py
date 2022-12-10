from day02.solution1 import parse_input, strip_n_replace


def test_strip_n_replace():
    assert strip_n_replace("A X, B Y, C Z") == ["AX", "BY", "CZ"]
    assert strip_n_replace("X Y, Z A") == ["XY", "ZA"]


def test_parser():
    assert parse_input("A X, B Y, C Z") == [("A", "X"), ("B", "Y"), ("C", "Z")]
    assert parse_input("X Y, Z A") == [("X", "Y"), ("Z", "A")]
