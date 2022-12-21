#!/usr/bin/python3

"""Define class Square."""


class Square:
    """A new square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set size of square."""
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set position of the square."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return("")
