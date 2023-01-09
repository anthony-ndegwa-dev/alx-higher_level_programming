#!/usr/bin/python3
"""Inheritance class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits BaseGeometry"""

    def __init__(self, width, height):
        """Initialize instances"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
