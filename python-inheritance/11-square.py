#!/usr/bin/python3
''' This Module creates a class Square that inherits from Rectangle '''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' This class defines a Square '''
    def __init__(self, size):
        ''' This function initializes a Square '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        ''' This function returns a string representation of a Square '''
        return "[Square] {}/{}".format(self.__size, self.__size)
