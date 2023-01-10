#!/usr/bin/python3
"""Function to return dictionary description with simple data structure
for JSON serialization of an object"""


def class_to_json(obj):
    """Return dictionary description with simple data structure"""
    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    return dic
