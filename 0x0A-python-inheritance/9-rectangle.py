#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize instances.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method to return area"""

        return self.__width * self.

    def __str__(self):
        """Returns the printable string"""

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
