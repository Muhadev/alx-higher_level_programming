#!/usr/bin/env python3
def no_c(my_string):
    result = ""
    for char in range(len(my_string)):
        if my_string[char] != 'c' and my_string[char] != 'C':
            result += my_string[char]
    return result
