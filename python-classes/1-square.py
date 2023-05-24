#!/usr/bin/python3
"""Module that creates a class, square"""


class Square:
""""Is an empty class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        """"function that creates a private instance size"""
        self.__size = size