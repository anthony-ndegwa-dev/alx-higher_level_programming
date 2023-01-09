#!/usr/bin/python3
"""Class that raises an Exception"""


class BaseGeometry:
    """Raise an Exception area() is not implemented"""

    def area(self):
        raise Exception("area() is not implemented")
