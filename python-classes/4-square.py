#!/usr/bin/python3
"""This module creates a class Square
"""


class Square:
    """This class creates a private instance attribute size
    """
    def __init__(self, size=0):
        """This function creates a private instance size
        """
        self.__size = size

    def area(self):
        """This function returns the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """This function returns the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This function sets the size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
