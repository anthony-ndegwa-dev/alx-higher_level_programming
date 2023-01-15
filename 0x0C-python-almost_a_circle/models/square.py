#!/usr/bin/python3
"""A class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class inherits from Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width)
