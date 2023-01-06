from day06.marker_finder import check_unique, find_marker_start, get_chunk


class TestMarkerFinder:
    def test_get_chunk(self):

        assert get_chunk("cdefadws", 4, 0) == "cdef"
        assert get_chunk("12345678911111", 4, 5) == "6789"

    def test_check_unique(self):

        assert check_unique("cdef", 4) == True
        assert check_unique("abcd", 4) == True

        assert check_unique("aabb", 4) == False
        assert check_unique("123", 4) == False

    def test_find_marker_start(self):

        assert find_marker_start("cdefg", 4) == 4
        assert find_marker_start("aabcde", 4) == 5
        assert find_marker_start("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11
        assert find_marker_start("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
        assert find_marker_start("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
