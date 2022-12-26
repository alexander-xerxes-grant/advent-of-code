from day06.solution1 import get_last_4_char


def test_get_last_4_char():
    assert get_last_4_char("cdef", 4) == "cdef"
    assert get_last_4_char("1", 1) == "1"
    assert get_last_4_char("123456789", 9) == "6789"
