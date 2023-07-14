#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

# make dict for each monkey,
"""monkey_1 = {'items': [99, 67, 92, 61, 83, 64, 98], 'inspection_counter':0, 'monkey_name': 0}"""

# create function which takes the monkey name as an argument
# and calculates the worry level

# what monkey to throw to?
# function that takes a throwing_monkey_name and a worry_level
# and returns a catching_monkey_name

# another function then reads this output and
# gets adds the relevant item to the catching monkey's inventory

#
# take item number
# calculate worry
# determine which monkey to throw to
# update monkey's item lists
# increment inspection count
# move to next monkey

import operator
from typing import List

operand_lookup_table = { "+": operator.add, "-": operator.sub, "*": operator.mul, operator.mod: "/"}




def get_input(filename):
    with open(filename) as f:
        lines = f.read()
        lines_split = lines.split("\n\n")
        monkey_info = [x.split("\n") for x in lines_split]
        
        return monkey_info
    
def create_monkey_dict(monkey_info: List[List[str]]) -> dict:
        monkey_dict ={}
        monkey_dict["name"] = monkey_info[0].replace(':', '').split(' ')[-1]
        items_str = monkey_info[1].split(': ')[-1].split(', ')
        monkey_dict["items"] = [int(x) for x in items_str]
        monkey_dict["inspection_counter"] = 0
        operand_line = monkey_info[2].split(' ')
        monkey_dict["operand"] = operand_line[-2]
        monkey_dict["operation_value"] = int(operand_line[-1])
        monkey_dict["test_criteria"] = int(monkey_info[3].split(" ")[-1])
        monkey_dict["monkey_true"] = monkey_info[4].split(" ")[-1]
        monkey_dict["monkey_false"] = monkey_info[5].split(" ")[-1]
        
        return monkey_dict
    
def create_list_monkey_dicts(filename):
    monkey_input = get_input(filename)
    monkey_list_dicts = []
    for monkey in monkey_input:
        monkey_list_dicts.append(create_monkey_dict(monkey_info=monkey))
    
    return monkey_list_dicts



def calculate_worry(item, operand, operation_value):
    operand = operand_lookup_table[operand]
    worry_score = math.floor(operand(item, operation_value) / 3)
    return worry_score


def decide_monkey(input_monkey: dict) -> int:
    output_monkey = []
    for item in input_monkey["items"]:
        new_worry_score = calculate_worry(item, input_monkey["operand"], input_monkey["operation_value"])
        if new_worry_score % input_monkey["test_criteria"] == 0:
            resulting_monkey = input_monkey["monkey_true"]
        else:
            resulting_monkey = input_monkey["monkey_false"]
            
        output_monkey.append({"item": new_worry_score, "output_monkey": resulting_monkey})

    return output_monkey
    
def update_monkey_dict(monkey, list_of_items_and_monkeys):
    
    list_of_items = []
    for element in list_of_items_and_monkeys:
        print(element)
        if element["output_monkey"] == monkey:
            list_of_items_and_monkeys.append(element["item"])
    return list_of_items
            
        






if __name__ == '__main__':
    test_input = '/Users/AGrant/Development/Personal/advent-of-code/python/day11/inputs/test_input.txt'
    create_list_monkey_dicts(test_input)
    
    
