#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []  # Initialize an empty list to store the boolean values

    for num in my_list:
        is_divisible = num % 2 == 0  # Check if the number is divisible by 2
        result.append(is_divisible)  # Append the boolean value to the result list

    return result
