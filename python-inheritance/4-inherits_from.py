#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class.
    False if obj is an instance of a_class itself or not related.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
