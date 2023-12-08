#!/usr/bin/python3
"""
function that reads a text file
(UTF8) and prints it to stdout
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        attributes = vars(self)
        serializable_dict = {}

        for attr, value in attributes.items():
            if isinstance(value, (list, dict, str, int, bool)):
                serializable_dict[attr] = value
        return serializable_dict
