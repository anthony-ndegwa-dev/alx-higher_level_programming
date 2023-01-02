#!/usr/bin/python3

"""This is a module for adding numbers"""


def add_integer(a, b=98):
    """Add two integer and/or float numbers

    Args:
    a: first number
    b: second number

    Raise:
    TypeError: if a or b aren't integer or float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)
