#!/usr/bin/python3

"""Module restricting user to create first_name instance attributes"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """Initialization"""
        pass
