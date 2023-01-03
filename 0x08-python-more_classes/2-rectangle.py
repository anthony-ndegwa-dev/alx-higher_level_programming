#!/usr/bin/python3

"""Define Rectangle class"""


class Rectangle:

    """Define rectangle"""

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = 

    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of rectangle"""
        return self.

    @height.setter
    def height(self, value):
        """Set height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to calculate area of rectangle"""
        return self.width * self.

    def perimeter(self):
        """Method to calculate perimeter of rectangle"""
        return 0

    return (2 * self.width) + (2 * self.height)
