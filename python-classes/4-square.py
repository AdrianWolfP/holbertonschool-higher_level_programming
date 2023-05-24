#!/usr/bin/python3
"""Module that creates a class, square"""


class Square:
    """Class that creates a private instance attribute size"""
    def __init__(self, size=0):
        """function that creates a private instance size"""
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
    self.__size = size

def area(self):
    """area of square"""
    return self.__size

@property
def size(self):
    return self.__size ** 2

@size.setter
def size(self, value):
    self.__size = value
    if not isinstance(self.__size, int):
        raise TypeError("Size must be an integer")
    if self.__size < 0:
        raise ValueError("Size must be >= 0")