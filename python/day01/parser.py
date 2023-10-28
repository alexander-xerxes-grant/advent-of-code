def parse_item(item):
    try:
        return int(item)
    except ValueError:
        raise ValueError(f"Invalid input: {item}")


def parse_calories(input_list):

    result = []
    temp_list = []

    for item in input_list:
        if item == "":
            if len(temp_list) > 0:
                result.append(temp_list)
                temp_list = []
        else:
            temp_list.append(parse_item(item))

    result.append(temp_list)

    return result
