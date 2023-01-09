#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Inheritance class"""


class Rectangle(BaseGeometry):
    """A class that inherits BaseGeometry"""

    def __init__(self, width, height):
        """Initialize instances"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
