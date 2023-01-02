#!/usr/bin/python3

"""

A module composed of a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """Function that divides the numbers of a matrix

    Args:
    matrix: list of a lists of integers/floats
    div: number which divides the matrix

    Returns:
    New matrix with the result of the division

    Raises:
    TypeError: 
    If the elements of the matrix aren't lists
    If the elements of the lists aren't integers or floats
    If div is not an integer or float number
    If the lists of the matrix don't have the same size

    ZeroDivisionError: If div is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    type_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(type_msg)

    len_e = 0
    size_msg = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(type_msg)

        if len_e != 0 and len(elems) != len_e:
            raise TypeError(size_msg)

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(type_msg)

        len_e = len(elems)
        new_lst = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
        return (new_lst)
