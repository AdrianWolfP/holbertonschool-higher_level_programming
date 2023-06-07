#!/usr/bin/python3
''' this module creates a class Square that inherits from Rectangle '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' This class defines a Square inherited from Rectangle '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' Construction Juntction Square's my function! '''
        self.integer_validator("width", size)
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' returns string representation of Square '''
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size
            )

    @property
    def size(self):
        ''' size getter '''
        return self.width

    @size.setter
    def size(self, value):
        ''' Would you like to supersize that? '''
        self.integer_validator("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' updates attributes of Square '''
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif args is None or len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        ''' returns the dictionary representation of a Square '''
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
