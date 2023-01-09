#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """Public instance method that prints the list sorted (ascending sort)"""

    def print_sorted(self):
        get_list = self.copy()
        get_list.sort()
        print(get_list)
