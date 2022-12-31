def parse_input(input):
    current = []

    for line in input:
        if line:
            current.append(int(line))
        else:
            yield current
            current = []
    if current:
        yield current


def sum_per_elf(input):
    return (sum(elf) for elf in parse_input(input))
