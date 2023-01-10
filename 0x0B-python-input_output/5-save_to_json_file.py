#!/usr/bin/python3
"""Function to write to a text file using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Write to a text file using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
