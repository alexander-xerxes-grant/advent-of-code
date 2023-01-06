from day06.solution1 import solve


def test_solve():

    assert solve("cdefg") == 4
    assert solve("aabcde") == 5
    assert solve("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
    assert solve("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert solve("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
