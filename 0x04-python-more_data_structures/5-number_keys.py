#!/usr/bin/python3

def number_keys(a_dictionary):
    count = 0

    list_keys = list(a_dictionary.keys())
    for i in list_keys:
        count += 1

    return (count)
