#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Creates a new list with an updated element at a specific index."""
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
