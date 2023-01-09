#!/usr/bin/python3
"""Class that raises an Exception"""


class BaseGeometry:
    """Raise an Exception area() is not implemented"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates values"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""Rectangle class inheriting BaseGeometry class"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Initialize instances"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
