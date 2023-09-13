import pytest

from ..parser import parse_input


class TestParser:
    def test_parse_input(self):
        assert list(parse_input(["1", "69", "420", "", "66"])) == [
            [1, 69, 420],
            [66],
        ]

    # assert list(parse_input(["1", "", "69", "420", "66", ""])) == [
    #     [1],
    #     [69, 420, 66],
    # ]


# def test_sum_per_elf():
#     assert list(sum_per_elf(["1", "69", "420", "", "66"])) == [490, 66]
#     assert list(sum_per_elf(["1", "", "69", "420", "66", ""])) == [1, 555]


# ["1", "69", "420", "", "66"] [[1, 69, 420], [66]]