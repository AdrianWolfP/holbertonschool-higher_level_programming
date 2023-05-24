#!/usr/bin/python3
"""Empty class that defines a square"""


class Square:
    """Class defines a square"""
    def __init__(self, size=0):
        """Initializes a simple square"""
        self.__size = size

    def area(self):
        """Area of square"""
        return self.__size ** 2
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

        def my_print(self):
            if self.__size == 0:
                print()
            else:
                for i in range(self.__size):
                    print("#" * self.__size)
                    