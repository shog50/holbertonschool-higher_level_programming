#!/usr/bin/python3
"""
Module for adding two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: First number (must be an integer or float).
        b: Second number (must be an integer or float, default is 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
