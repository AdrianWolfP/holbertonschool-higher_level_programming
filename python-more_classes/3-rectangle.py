#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle by:
    Private instance attribute: width
    Private instance attribute: height
    Instantiation with optional width and height: def __init__
    (self, width=0, height=0):
    Public instance method: def area(self): that returns the
    rectangle area
    Public instance method: def perimeter(self): that returns the
    rectangle perimeter:
    print() and str() should print the rectangle with the char #:
        if width or height is equal to 0, return an empty string
"""


class Rectangle:
    """Initializes the Rectangle data"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """Getter for private attribute width"""
    @property
    def width(self):
        return self.__width

    """Setter for private attribute width"""
    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = int(value)

    """Getter for private attribute height"""
    @property
    def height(self):
        return self.__height

    """Setter for private attribute height"""
    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = int(value)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            perimeter = (self.width * 2) + (self.height * 2)
            return perimeter

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            string = ""
            for i in range(self.height):
                string += "#" * self.width
                if i < self.height - 1:
                    string += "\n"
            return string
