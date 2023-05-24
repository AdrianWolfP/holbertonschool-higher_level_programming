#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle by:
    Private instance attribute: width
    Private instance attribute: height
    Instantiation with optional width and height: def __init__
    (self, width=0, height=0):
    Public class attribute: number_of_instances
    Initialized to 0
    Incremented during each new instance instantiation
    Decremented during each instance deletion
    Public class attribute: print_symbol
    Initialized to #
    Used as symbol for string representation
    Can be any type
    Public instance method: def area(self): that returns the
    rectangle area
    Public instance method: def perimeter(self): that returns the
    rectangle perimeter:
    If width or height is equal to 0, perimeter is equal to 0
    print() and str() should print the rectangle with the character
    stored in print_symbol:
        if width or height is equal to 0, return an empty string
    repr() should return a string representation of the rectangle
    to be able to recreate a new instance by using eval()
    Print the message Bye rectangle... (... being 3 dots not ellipsis)
    when an instance of Rectangle is deleted
"""


class Rectangle:
    """Class Rectangle that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    """Initializes the Rectangle data"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        if self.width > 0 and self.height > 0:
            return (self.width + self.height) * 2
        else:
            return 0

    def __str__(self):
        string = ""
        if self.width > 0 and self.height > 0:
            for i in range(self.height):
                string += str(self.print_symbol) * self.width
                if i < self.height - 1:
                    string += "\n"
        return string

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
