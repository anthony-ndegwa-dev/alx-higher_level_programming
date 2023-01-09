#!/usr/bin/python3
"""Function to return True if object is exactly an instance of the
specified class, otherwise False"""


def is_same_class(obj, a_class):
    """Returns True if the object is an instance of the specified class"""

    return isinstance(obj, a_class)
