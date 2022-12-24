from day01.solution2 import solver


def test_solver():
    assert (
        solver(
            [
                "1",
                "",
                "2",
                "",
                "3",
                "",
                "4",
            ]
        )
        == 9
    )
