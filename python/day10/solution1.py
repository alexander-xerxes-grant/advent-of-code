#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Cathode:

    SNAPSHOT_TOTAL = 0
    SNAPSHOTS = [20, 60, 100, 140, 180, 220]
    CMD_CYCLES = {"noop": 1, "addx": 2}

    def __init__(self):
        self.cycles = 0
        self.cmd_reg = 1

    def parse_cmd(self, cmd):
        command, _, val = cmd.partition(" ")
        if command == "noop":
            val = 0
        return self.CMD_CYCLES.get(command), int(val)

    def run_command(self, cycle: int, val: int):
        for i in range(cycle):
            self.cycles += 1
            if self.is_snapshot(self.cycles) is True:
                self.SNAPSHOT_TOTAL += self.cycles * self.cmd_reg
        self.cmd_reg += val

    def is_snapshot(self, cycles):
        return cycles in self.SNAPSHOTS


def solve(puzzle_input):
    ct = Cathode()
    for cmd in puzzle_input:
        cycle, val = ct.parse_cmd(cmd)
        ct.run_command(cycle, val)
    return ct.SNAPSHOT_TOTAL


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solve, __file__)
