#!/usr/bin/python3
""" Python script to find a peak inside a list """


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    center = int(length / 2)
    li = list_of_integers

    if center - 1 < 0 and center + 1 >= length:
        return li[center]
    elif center - 1 < 0:
        return li[center] if li[center] > li[center + 1] else li[center + 1]
    elif center + 1 >= length:
        return li[center] if li[center] > li[center - 1] else li[center - 1]

    if li[center - 1] < li[center] > li[center + 1]:
        return li[center]

    if li[center + 1] > li[center - 1]:
        return find_peak(li[center:])
    return find_peak(li[:center])
