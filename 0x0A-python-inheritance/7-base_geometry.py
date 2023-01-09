#!/usr/bin/python3
"""Class that raises an Exception"""


class BaseGeometry:
    """Raise an Exception area() is not implemented"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates values"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
