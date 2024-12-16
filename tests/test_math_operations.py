from mainpython import math_operations


def test_add():
    assert math_operations.add(2, 3) == 5


def test_subtract():
    assert math_operations.subtract(5, 3) == 2
