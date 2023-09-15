from itertools import groupby


def parse_input(input_list):

    return [[int(item) for item in group] for _, group in groupby(input_list, lambda x: x == '') if not _]
