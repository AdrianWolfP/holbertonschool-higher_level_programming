#!/usr/bin/python3
""""module that creates a empty class"""
class Square:
    def __init__(self, size=0):
        """"function that creates a private instance size"""
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be <= 0")
        self.__size = size