#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import default_timer as timer

from .input import get_input


def run_solver(solver, path_str, filename="input.txt"):
    start = timer()

    input_text = get_input(path_str, filename)
    solution = solver(input_text)

    print(solution)

    end = timer()
    print()
    print("-" * 80)
    print("Time elapsed: {:.3f}s".format(end - start))
