def parse_input(input_list):
    # input list is the return from get_input

    # I want to parse the list of strings, a list of lists
    # Where each list represents the calories carried by one elf
    result = []
    temp_list = []

    for i in input_list:
        if i == '':
            result.append(temp_list)
            temp_list = []
        else:
            temp_list.append(int(i))
    result.append(temp_list)

    return result
