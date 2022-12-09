# Receive a file
# Open the file
# Read the file
# Parse into a list of strings
# each string is made up of two compartments, of equal length
# find the common letter in each compartment
# assign a-Z to 1-56 (dict)
# sum value of letters
# where value is 1-56 (a-z)


def parse_input(filepath):
    with open(filepath, "r") as f:
        return f.read().splitlines()


def split_rucksacks(rucksacks):
    pass
