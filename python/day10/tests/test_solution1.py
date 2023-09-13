#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest.mock import MagicMock

import pytest

from shared import get_input

from .. import solution1
from ..solution1 import Cathode


class TestSolution:
    @pytest.fixture
    def ct(self):
        yield Cathode()

    @pytest.fixture
    def puzzle_input(self):
        yield get_input(solution1.__file__, "test_input.txt")

    def test_parse_cmd_returns_cmd_val(self, ct):
        cycles, val = ct.parse_cmd("addx 24")
        assert cycles == 2
        assert val == 24
        cycles, val = ct.parse_cmd("noop")
        assert cycles == 1
        assert val == 0

    def test_run_command(self, ct):
        assert ct.run_command(2, 21) == None
        assert ct.cycles == 2
        assert ct.cmd_reg == 22

        assert ct.run_command(1, 0) == None
        assert ct.cycles == 3
        assert ct.cmd_reg == 22

        assert ct.run_command(2, -22) == None
        assert ct.cycles == 5
        assert ct.cmd_reg == 0

    def test_run_command_calls_snapshot(self, ct):
        ct.is_snapshot = MagicMock()
        ct.run_command(2, -22)
        ct.is_snapshot.assert_called_with(2)

    def test_run_command_snapshot_update(self, ct):
        ct.is_snapshot = MagicMock(return_value=True)
        ct.run_command(2, -22)
        assert ct.SNAPSHOT_TOTAL == 3

    def test_run_command_does_snapshot_update(self, ct):
        ct.is_snapshot = MagicMock(return_value=False)
        ct.run_command(2, -22)
        assert ct.SNAPSHOT_TOTAL == 0

    def test_run_command_recognise_snapshot(self, ct):
        ct.run_command(19, 1)
        ct.run_command(2, 1)
        assert ct.SNAPSHOT_TOTAL == 40

    def test_is_snapshot(self, ct):
        assert ct.is_snapshot(0) is False

        assert ct.is_snapshot(20) is True

        assert ct.is_snapshot(60) is True

        assert ct.is_snapshot(21) is False

        assert ct.is_snapshot(40) is False
