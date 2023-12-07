#!/usr/bin/python3
"""
function that reads a text file
(UTF8) and prints it to stdout
"""
import json


def save_to_json_file(my_obj, filename):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
