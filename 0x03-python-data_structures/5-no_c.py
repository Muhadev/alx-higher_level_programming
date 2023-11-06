#!/usr/bin/env python3
def no_c(my_string):
    result = ""
    for char in range(len(my_string)):
        if (my_string[char] == 'c') or (my_string[char] == 'C'):
            result
        else:
            result += my_string[char]
    return result
