#!/usr/bin/python3
"""
Module for defining a Square class.
"""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initializes a Square instance with a given size.
        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and returns the current square area."""
        return self.__size ** 2
