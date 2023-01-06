def get_chunk(input: str, marker_length: int, i: int) -> str:
    return input[i : i + marker_length]


def check_unique(chunk: str, marker_length: int) -> bool:
    return len(chunk) and len(set(chunk)) == marker_length


def find_marker_start(input: str, marker_length: int) -> int:
    for i in range(0, len(input) - marker_length):
        if len(set(get_chunk(input, marker_length, i))) == marker_length:
            return i + marker_length
