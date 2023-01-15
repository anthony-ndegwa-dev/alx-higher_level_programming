#!/usr/bin/python3
"""Module containing class Rectangle that inherits from Base """
from base import Base


clase Rectangle(Base):
    """The Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instances"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

