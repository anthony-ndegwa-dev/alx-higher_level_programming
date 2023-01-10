#!/usr/bin/python3
"""A function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Append a string in text file and return number of characters added"""

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
