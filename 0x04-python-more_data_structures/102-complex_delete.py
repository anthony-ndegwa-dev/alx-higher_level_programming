#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys_list = list(a_dictionary.keys())

    for i in keys_list:
        if value == a_dictionary.get(i):
            del a_dictionary[i]

    return (a_dictionary)
