import pytest
from shared import get_input

from ..solution1 import check_command


class TestSolution1:
    @pytest.fixture
    def challenge_input(self):
        yield get_input(__file__, "test_input.txt")

    def test_check_command(self, challenge_input):
        assert check_command(challenge_input) == ""
