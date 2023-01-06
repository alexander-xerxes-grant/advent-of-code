from day06.solution2 import solve


def test_solve():
    assert solve("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert solve("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    "nppdvjthqldpwncqszvftbrmjlhg" == 23
    assert solve("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert solve("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
