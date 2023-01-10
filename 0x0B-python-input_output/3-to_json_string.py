#!/usr/bin/python3
"""A function to return JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """Return JSON representation of string"""

    return json.dumps(my_obj)
