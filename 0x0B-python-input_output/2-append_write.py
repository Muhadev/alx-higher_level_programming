#!/usr/bin/python3
"""
function that reads a text file
(UTF8) and prints it to stdout
"""


def append_write(filename="", text=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
