#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()
    sum_of_unique_integers = 0
    for number in my_list:
        if number not in unique_integers:
            unique_integers.add(number)
            sum_of_unique_integers += number
    return sum_of_unique_integers
