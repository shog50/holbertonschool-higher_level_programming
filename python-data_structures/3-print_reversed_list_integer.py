#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order using str.format()"""
    if my_list:
        for num in reversed(my_list):
            print("{:d}".format(num))
