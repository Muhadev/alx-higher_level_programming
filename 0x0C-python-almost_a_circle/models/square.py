#!/usr/bin/python3
"""
the class Rectangle that inherits from Base
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle:"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor:"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The overloading __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)
