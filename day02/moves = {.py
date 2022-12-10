from typing import Dict, Iterable, List, Tuple


def parse_input(input: Iterable[str]) -> List[Tuple[str, str]]:
    # Use the split and strip methods to split each string on the "," character and remove any leading or trailing whitespace
    pairs = [tuple(x.split(" ")) for x in input]
    # Use the zip function to combine the characters in each string into pairs
    tuples = [tuple(zip(x[0::2], x[1::2])) for x in pairs]
    # Flatten the list of tuples
    return [item for sublist in tuples for item in sublist]


# Example input strings
input_strs = ["A X, B Y, C Z", "D P, E R, F S"]

# Parse the input strings
parsed_input = parse_input(input_strs)

# The parsed input should be [("A", "X"), ("B", "Y"), ("C", "Z"), ("D", "P"), ("E", "R"), ("F", "S")]
print(parsed_input)
