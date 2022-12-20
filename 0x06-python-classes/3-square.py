#!/usr/bin/python3

""" A class to define a square by its size """


class Square:
    """ Initialize the square object """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """ Method to return area of square """
    def area(self):
        return (self.__size ** 2)
