#!/usr/bin/python3
"""Empty class that defines a square"""


class Square:
    """Class defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size
    
    @property
    def position(self):
        return self.__position
    
    def area(self):
        """Area of square"""
        return self.__size ** 2
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = value

        @position.setter
        def position(self, value):
            if type(value) is not tuple or len(value) != 2:
                raise TypeError("Position must be a tuple of 2 positive integers")
            elif type(value [0]) is not int or value[0] < 0:
                raise TypeError("Position must be a tuple of 2 positive integers")
            elif type(value[1]) is not int or value[1] < 0:
                raise TypeError("Position must be a tuple of 2 positive integers")
            self.__position = value

        def my_print(self):
            if self.__size == 0:
                print()
            else:
                for i in range(self.position[1]):
                    print()
                for i in range(self.size):
                    for j in range(self.position[0]):
                        print(end=" ")
                    for k in range(self.size):
                        print("#", end="")
                    print()
