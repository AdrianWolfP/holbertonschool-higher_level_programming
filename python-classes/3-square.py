#!/usr/bin/python3
"""class that creates a class, square"""
class Square:
    """fucntion creates a private instance size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size

    def area(self):
        """fucntion that returns current square area"""
        return self._size ** 2