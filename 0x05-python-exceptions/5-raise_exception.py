#!/usr/bin/python3

def raise_exception():
    """that raises a type exception."""
    try:
        result = 10 + "hello"
    except TypeError:
        raise TypeError("Exception raised")
