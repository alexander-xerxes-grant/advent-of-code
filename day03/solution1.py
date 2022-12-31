from day03.values_dict import create_value_dict

# Parse into a list of strings
# each string is made up of two compartments, of equal length
# find the common letter in each compartment
# assign a-Z to 1-52 (dict)
# sum value of letters
# where value is 1-52 (a-z)


def split_items(items: str):
    return [items[: len(items) // 2], items[len(items) // 2 :]]


def find_common_letters(items: str):
    compartment_1 = set(items[0])
    compartment_2 = set(items[1])
    return "".join(compartment_1.intersection(compartment_2))


# Use the following line instead if the input is a single line
# def solver(input: str) -> str:
def solver(input_list) -> str:
    total = 0
    for input in input_list:
        split = split_items(input)
        common_letters = find_common_letters(split)
        value_dict = create_value_dict()
        total += value_dict.get(common_letters)

    return total


if __name__ == "__main__":
    from shared import run_solver

    run_solver(solver, __file__)
