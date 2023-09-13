#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from ..solution1 import (
    calculate_worry,
    create_list_monkey_dicts,
    create_monkey_dict,
    decide_monkey,
    get_input,
    update_monkey_dict,
)


@pytest.fixture
def filename():
    return "/Users/AGrant/Development/Personal/advent-of-code/python/day11/inputs/test_input.txt"


@pytest.fixture
def monkey_dict():

    return {
        "name": "0",
        "items": [79, 98],
        "inspection_counter": 0,
        "operand": "*",
        "operation_value": 19,
        "test_criteria": 23,
        "monkey_true": "2",
        "monkey_false": "3",
    }


class TestSolution:
    def test_get_input(self, filename):

        expected_output = [
            [
                "Monkey 0:",
                "  Starting items: 79, 98",
                "  Operation: new = old * 19",
                "  Test: divisible by 23",
                "    If true: throw to monkey 2",
                "    If false: throw to monkey 3",
            ],
            [
                "Monkey 1:",
                "  Starting items: 54, 65, 75, 74",
                "  Operation: new = old + 6",
                "  Test: divisible by 19",
                "    If true: throw to monkey 2",
                "    If false: throw to monkey 0",
            ],
            [
                "Monkey 2:",
                "  Starting items: 79, 60, 97",
                "  Operation: new = old * old",
                "  Test: divisible by 13",
                "    If true: throw to monkey 1",
                "    If false: throw to monkey 3",
            ],
            [
                "Monkey 3:",
                "  Starting items: 74",
                "  Operation: new = old + 3",
                "  Test: divisible by 17",
                "    If true: throw to monkey 0",
                "    If false: throw to monkey 1",
            ],
        ]

        assert get_input(filename) == expected_output
        assert isinstance(get_input(filename), list)

    def test_create_monkey_dict(self, filename):

        test_monkey = [
            "Monkey 0:",
            "  Starting items: 79, 98",
            "  Operation: new = old * 19",
            "  Test: divisible by 23",
            "    If true: throw to monkey 2",
            "    If false: throw to monkey 3",
        ]

        expected_output = {
            "name": "0",
            "items": [79, 98],
            "inspection_counter": 0,
            "operand": "*",
            "operation_value": 19,
            "test_criteria": 23,
            "monkey_true": "2",
            "monkey_false": "3",
        }

        assert create_monkey_dict(test_monkey) == expected_output

    def test_create_list_monkey_dicts(self):

        expected_output = [
            {
                "name": "0",
                "items": [79, 98],
                "inspection_counter": 0,
                "operand": "*",
                "operation_value": 19,
                "test_criteria": 23,
                "monkey_true": "2",
                "monkey_false": "3",
            },
            {
                "name": "1",
                "items": [2],
                "inspection_counter": 0,
                "operand": "+",
                "operation_value": 6,
                "test_criteria": 19,
                "monkey_true": "2",
                "monkey_false": "0",
            },
        ]

        actual_ouput = create_list_monkey_dicts(
            "/Users/AGrant/Development/Personal/advent-of-code/python/day11/inputs/test_monkey_file.txt"
        )

        assert actual_ouput == expected_output

    def test_calculate_worry_score(self):
        expected_output = 500

        monkey_dict = {
            "name": "Monkey 0",
            "items": [79, 98],
            "inspection_counter": 0,
            "operand": "*",
            "operation_value": 19,
            "test_critera": 23,
            "true_monkey": "2",
            "false_monkey": "3",
        }
        item = 79
        operand = "*"
        operation_value = 19

        actual_output = calculate_worry(item, operand, operation_value)

        assert actual_output == expected_output

    def test_decide_monkey(self, monkey_dict):
        expected_output = [
            {"item": 500, "output_monkey": "3"},
            {"item": 620, "output_monkey": "3"},
        ]

        actual_output = decide_monkey(monkey_dict)

        assert expected_output == actual_output

    def test_update_monkey_dict(self):
        monkey = "3"
        list_of_items_and_monkeys = [
            {"item": 500, "output_monkey": "3"},
            {"item": 620, "output_monkey": "3"},
        ]

        list_of_items = [500, 620]

        assert update_monkey_dict(monkey, list_of_items_and_monkeys) == [
            {"item": 500, "output_monkey": "3"},
            {"item": 620, "output_monkey": "3"},
        ]
