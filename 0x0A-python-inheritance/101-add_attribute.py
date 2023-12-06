#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr_name, attr_value):
    if hasattr(obj, '__dict__'):
        obj.__setattr__(attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
