#!/usr/bin/python3
""" this module creates an empty class Rectangle
"""


class Rectangle:
    """ class Rectangle that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initializes a rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ gets width of rectangle
        """
        return self.__width

    @property
    def height(self):
        """ gets height of rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ sets width of rectangle
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets height of rectangle
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ returns area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """ returns perimeter of rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ returns a string of # as a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ((str(self.print_symbol) * self.__width + '\n') *
                self.__height)[:-1]

    def __print__(self):
        """prints rectangle
        """
        print(str(self))

    def __repr__(self):
        """ returns a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ deletes an instance of Rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle vassed on the area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 == area_2 or area_1 > area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance with width == height == size
        """
        return cls(size, size)
