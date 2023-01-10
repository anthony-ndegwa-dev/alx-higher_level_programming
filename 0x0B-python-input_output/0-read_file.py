#!/usr/bin/python3
"""A function that reads a text file"""


def read_file(filename=""):
    """Read a text file and prints it to stdout"""

    with open(filename, "r", encoding='utf-8') as f:
        read_file = f.read()
        print(read_file, end='')
