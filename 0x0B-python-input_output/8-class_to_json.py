#!/usr/bin/python3
"""
function that reads a text file
(UTF8) and prints it to stdout
"""

def class_to_json(obj):
    """Get all attributes of the object"""
    attributes = vars(obj)
    serializable_dict = {}

    for attr, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[attr] = value
    return serializable_dict
