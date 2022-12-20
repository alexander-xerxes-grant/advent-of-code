from day05.solution1 import parse_lines


def test_parse_lines():
    input_string = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
"""
    assert parse_lines(input_string) == [
        "[D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3",
    ]
