from day01.solution1 import parse_input, sum_per_elf, solver


def test_parse_input():
    assert list(parse_input(["1", "69", "420", "", "66"])) == [
        [1, 69, 420],
        [66],
    ]
    assert list(parse_input(["1", "", "69", "420", "66", ""])) == [
        [1],
        [69, 420, 66],
    ]


def test_sum_per_elf():
    assert list(sum_per_elf(["1", "69", "420", "", "66"])) == [490, 66]
    assert list(sum_per_elf(["1", "", "69", "420", "66", ""])) == [1, 555]


def test_solver():
    assert solver(["1", "69", "420", "", "66"]) == 490
    assert solver(["1", "", "69", "420", "66", ""]) == 555
