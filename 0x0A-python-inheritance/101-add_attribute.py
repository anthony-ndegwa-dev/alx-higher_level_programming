#!/usr/bin/python3
"""function that adds a new attribute to an object if possible"""


def add_attribute(obj, name, value):
    """Add attribute to object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
