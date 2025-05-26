#!/usr/bin/python3
"""
This module provides a function that returns a list
of available attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of all attributes and methods
    available for the given object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the names of the object's
        attributes and methods.
    """
    return dir(obj)
