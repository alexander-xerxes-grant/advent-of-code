import string


def create_value_dict():
    values = list(string.ascii_lowercase + string.ascii_uppercase)
    value_dict = {value: index for index, value in enumerate(values, start=1)}

    return value_dict
