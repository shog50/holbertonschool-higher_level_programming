#!/usr/bin/python3
"""
Module for defining a Square class
"""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initializes a Square instance with a given size.
        Args:
            size: The size of the square (no type/value verification).
        """
        self.__size = size
