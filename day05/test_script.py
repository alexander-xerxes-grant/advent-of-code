def parse_input(filepath):
    with open(filepath) as f:
        stack_strings, instructions = (
            i.splitlines() for i in f.read().strip("\n").split("\n\n")
        )
    return stack_strings, instructions


stack_strings, instructions = parse_input("day05/test_input.txt")
print(stack_strings, instructions)

# stacks = {int(digit): [] for digit in stack_strings[-1].replace(" ", "")}

# indexes = [
#     index for index, char in enumerate(stack_strings[-1]) if char != " "
# ]


# def display_stacks():
#     print("\n\nStacks:\n")
#     for stack in stacks:
#         print(stack, stacks[stack], indexes)
#     print("\n")


# def load_stacks():
#     print(stack_strings)
#     for string in stack_strings[:-1]:
#         stack_num = 1
#         for index in indexes:
#             if string[index] != " ":
#                 stacks[stack_num].insert(0, string[index])
#             stack_num += 1


# load_stacks()
# display_stacks()
