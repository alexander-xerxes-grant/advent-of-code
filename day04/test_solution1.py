from day04.solution1 import parse_input, construct_ranges

# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8


def test_parse_input():
    assert parse_input("2-4,6-8") == [(2, 4), (6, 8)]
    assert parse_input("2-3, 4-5") == [(2, 3), (4, 5)]


def test_construct_ranges():
    assert calculate_ranges([(2, 3), (0, 4)]) == [range(2, 3), range(0, 4)]
