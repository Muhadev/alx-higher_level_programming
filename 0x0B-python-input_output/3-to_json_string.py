#!/usr/bin/python3
"""
function that reads a text file
(UTF8) and prints it to stdout
"""
import json


def to_json_string(my_obj):
    """reads a text file (UTF8) and prints it to stdout"""
    return json.dumps(my_obj)
