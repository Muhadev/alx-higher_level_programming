#!/usr/bin/python3
"""
function that reads a text file
(UTF8) and prints it to stdout
"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file"""
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
