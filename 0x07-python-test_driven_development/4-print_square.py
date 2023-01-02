#!/usr/bin/python3

"""This module prints square"""


def print_square(size):
    """
    Function prints a square with # character

    Raises:
    TypeError: If size is not an integer number
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
