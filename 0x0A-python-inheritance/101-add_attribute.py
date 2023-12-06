#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible.
    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if hasattr(obj, '__dict__'):
        obj.__setattr__(attr_name, attr_value)
    elif hasattr(obj, '__slots__') or hasattr(type(obj), '__slots__'):
        raise TypeError("can't add new attribute")
    else:
        raise TypeError("can't add new attribute")
