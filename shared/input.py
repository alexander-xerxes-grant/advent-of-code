#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def get_input(path_str, filename):
    inputs_dir = Path(path_str).parent.parent.parent / "advent-of-code"
    path = inputs_dir / Path(path_str).parent.name / filename

    with path.open() as f:
        result = f.read().splitlines()

    if len(result) == 1:
        return result[0]

    return result
