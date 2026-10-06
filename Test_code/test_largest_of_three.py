import sys
sys.path.insert(0, "code")

from largest_of_three import largest

def test_first_largest():
    assert largest(10, 5, 8) == 10

def test_second_largest():
    assert largest(3, 15, 7) == 15

def test_third_largest():
    assert largest(4, 9, 12) == 12