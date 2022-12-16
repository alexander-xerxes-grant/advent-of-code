from day04.solution2 import check_range_overlaps


def test_check_range_overlaps():
    assert check_range_overlaps([[2, 4], [6, 8]]) == 0
    assert check_range_overlaps([[2, 3], [0, 5]]) == 1
    assert check_range_overlaps([[10, 15], [9, 16]]) == 1
    assert check_range_overlaps([[1, 2], [2, 4]]) == 1
    assert check_range_overlaps([[2, 5], [3, 6]]) == 1
    assert check_range_overlaps([[9, 10], [3, 8]]) == 0
