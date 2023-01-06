#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def get_input(path_str, filename):

    path = Path(path_str).parent / "inputs" / filename

    with path.open() as f:
        result = f.read().splitlines()

    if len(result) == 1:
        return result[0]

    return result
