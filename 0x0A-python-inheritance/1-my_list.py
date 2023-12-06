#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """a class MyList that inherits from list"""
    def __init__(self):
        """a class MyList that inherits from list"""
        super().__init__()

    def print_sorted(self):
        """a class MyList that inherits from list"""
        sorted_list = sorted(self)
        print(sorted_list)
