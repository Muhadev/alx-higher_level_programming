#!/usr/bin/python3
"""
Write the first class Base:
"""


class Base:
    """
    Represent the base model.
    Represents the "base" for all other classes in projects 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
