#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """ Initialize new square."""
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        """Get size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """ Print the square with # character """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
