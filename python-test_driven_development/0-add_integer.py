#!/usr/bin/python3
"""
This module provides a function to add two integers.
Handles float overflow and NaN by raising a TypeError.
"""


def add_integer(a, b=98):
    """
    Adds two numbers after casting to int.
    Raises TypeError if inputs are not int or float,
    or if float is inf or NaN.

    Args:
        a: First number (int or float)
        b: Second number (int or float, default is 98)

    Returns:
        The integer addition of a and b.
    """
    # Check a
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if isinstance(a, float):
        if a == float('inf') or a == float('-inf') or a != a:
            raise TypeError("a must be an integer")

    # Check b
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(b, float):
        if b == float('inf') or b == float('-inf') or b != b:
            raise TypeError("b must be an integer")

    return int(a) + int(b)
