#!/usr/bin/python3
"""A function that returns True if object is an instance of a class
that inherited (directly or indirectly) from the specified class,
otherwise False."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a_class"""

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
