from day04.solution1 import check_range_in_range, parse_input, solver


def test_parse_input():
    assert parse_input("2-4, 6-8") == [[2, 4], [6, 8]]
    assert parse_input("2-3, 4-5") == [[2, 3], [4, 5]]


def test_check_range_in_range():
    assert check_range_in_range([[2, 4], [6, 8]]) == 0
    assert check_range_in_range([[2, 3], [0, 5]]) == 1
    assert check_range_in_range([[10, 15], [9, 16]]) == 1


def test_solver():
    assert (
        solver(
            [
                "2-4, 6-8",
                "2-3, 1-5",
                "5-7, 1-9",
            ]
        )
        == 2
    )
    assert solver(["2-4, 6-8", "2-3, 4-5"]) == 0
