#!/usr/bin/python3


""" Write class Rectangle that inherits from Base """


# imports the base class
from models.base import Base


class Rectangle(Base):
    """ Rectangle that inherits from Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor of the Rectangle class that inherits from Base class
        parameters: Calls super class with id: super()__init__(id) """
        super()__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

# getters and setters
    @property
    def width(self):
        """ Getter for the private instance attribute: """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for the __width of rectangle """
        if not isinstance(value, int:)
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """ getter for the private instance attribute """
        return self.__height
    
    @height.setter
    def height