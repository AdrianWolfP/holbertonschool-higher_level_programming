#!/usr/bin/python3
""" function that prints a square with the character # """


ErrMsg01 = "size must be an integer"
ErrMsg02 = "size must be >= 0"
ErrMsg03 = "size must be an integer"


def print_square(size):
    """ function that prints a square with the character # """
    if size is None:
        raise TypeError(ErrMsg01)
    if type(size) != int:
        raise TypeError(ErrMsg01)
    if size < 0:
        raise ValueError(ErrMsg02)
    if type(size) == float and size < 0:
        raise TypeError(ErrMsg03)
    else:
        for i in range(size):
            print("#" * size)
