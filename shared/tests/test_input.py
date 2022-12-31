#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from shared.input import get_input

BASE_PATH = Path(__file__).parent.parent / "test_fixtures/python/"


def test_single_line():
    path_str = BASE_PATH / "day01/some_file.py"
    result = get_input(path_str, "single_line_file.txt")

    assert result == "Hello, world"


def test_multi_line():
    path_str = BASE_PATH / "day02/some_file.py"
    result = get_input(path_str, "multi_line_file.txt")

    assert result == ["Hello, world", "Testing 123"]
