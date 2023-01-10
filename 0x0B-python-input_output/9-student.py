#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """Define a studen"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method to retrieve dictionary representation of Student instance"""
        return self.__dict__.copy()
