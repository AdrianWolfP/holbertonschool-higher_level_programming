#!/usr/bin/python3
""" function that divides all elements of a matrix """


ErrMsg01 = "matrix must be a matrix (list of lists) of integers/floats"
ErrMsg02 = "Each row of the matrix must have the same size"
ErrMsg03 = "div must be a number"
ErrMsg04 = "division by zero"


def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix """
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(ErrMsg01)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(ErrMsg01)
        if len(row) != len(matrix[0]):
            raise TypeError(ErrMsg02)
        for num in row:
            if type(num) is not int and type(num) is not float:
                raise TypeError(ErrMsg01)
    if type(div) is not int and type(div) is not float:
        raise TypeError(ErrMsg03)
    if div == 0:
        raise ZeroDivisionError(ErrMsg04)
    return [[round(num / div, 2) for num in row] for row in matrix]
