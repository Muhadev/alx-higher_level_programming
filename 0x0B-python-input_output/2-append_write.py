#!/usr/bin/python3
"""
function that reads a text file
(UTF8) and prints it to stdout
"""


def append_file(filename="", text=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.append(), end="")
