from ..parse_sum import parse_input, sum_per_elf


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
