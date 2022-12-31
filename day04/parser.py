def parse_input(line: str):
    elves = line.split(",")
    ranges = [list(map(int, elf.split("-"))) for elf in elves]
    return ranges
