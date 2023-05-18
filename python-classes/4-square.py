#!/usr/bin/python3
def __init__(self, size=0):
    if not isinstance(size, int):
        raise TypeError("Size must be an integer")
    if size < 0:
        raise ValueError("Size must be >= 0")
    self.__size = size

def area(self):
    return self.__size

def size(self):
    return self.__size ** 2

def size(self):
    return self.__size

def size(self, value):
    self.__size = value
    if not isinstance(self.__size, int):
        raise TypeError("Size must be an integer")
    if self.__size < 0:
        raise ValueError("Size must be >= 0")