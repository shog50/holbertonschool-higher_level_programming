#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Returns a list of True/False indicating if each element is a multiple of 2."""
    return [num % 2 == 0 for num in my_list]
