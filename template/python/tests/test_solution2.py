#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from shared import get_input

from .. import solution2
from ..solution2 import solve


class TestSolution:
    @pytest.fixture
    def puzzle_input(self):
        yield get_input(solution2.__file__, "test_input.txt")

    def test_solver(self, puzzle_input):
        assert solve(puzzle_input) == "lorem ipsum?"
