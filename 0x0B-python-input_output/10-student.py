#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """Define a studen"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method to retrieve dictionary representation of Student instance"""
        obj = self.__dict__.copy()
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return obj

            my_list = {}
            for i in range(len(attrs)):
                for j in obj:
                    if attrs[i] == j:
                        my_list[j] = obj[j]
            return my_list

        return obj
