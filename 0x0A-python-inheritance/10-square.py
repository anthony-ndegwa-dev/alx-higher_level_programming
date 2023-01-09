#!/usr/bin/python3
"""Define a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class to define a Square from Rectangle class """
    def __init__(self, size):
        """ Method that initializes a Square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
