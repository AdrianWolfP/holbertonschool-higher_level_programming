#!/usr/bin/python3
"""This module creates a class Square
"""


class Square:
    """This class is an empty class
    """
    def __init__(self, size=0):
        """This function creates a private instance size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """This function returns the current square area
        """
        return self.__size ** 2
