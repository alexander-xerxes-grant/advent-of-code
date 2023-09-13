#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest.mock import patch

import pytest

from shared.solve import run_solver


@pytest.fixture
def get_input():
    with patch("shared.solve.get_input", autospec=True) as mock:
        mock.return_value = "Some input"
        yield mock


@pytest.fixture
def timer():
    with patch("shared.solve.timer", autospec=True) as mock:
        yield mock


def test_run_solver_prints_expected(capsys, get_input, timer):
    expected_output = (
        "SOME INPUT\n"
        "\n"
        "----------------------------------------"
        "----------------------------------------\n"
        "Time elapsed: 0.123s\n"
    )
    timer.side_effect = [987654.321, 987654.444]

    run_solver(lambda x: x.upper(), __file__)
    assert capsys.readouterr().out == expected_output


def test_run_solver_calls_get_input_with_default_filename(get_input):
    run_solver(lambda x: x, "some path")

    get_input.assert_called_once_with("some path", "input.txt")


def test_run_solver_calls_get_input_with_provided_filename(get_input):
    run_solver(lambda x: x, "some path", "test_input.txt")

    get_input.assert_called_once_with("some path", "test_input.txt")
