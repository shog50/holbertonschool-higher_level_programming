#!/usr/bin/python3
"""Module for defining a Square class.
"""


class Square:
    """Represents a square with a private size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance with a given size and position.

        Args:
            size (int, optional): The size of the square (default is 0).
            position (tuple, optional): The position of the square
                (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is not a tuple
                of two positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size  # Using setter for validation
        self.position = position  # Using setter for validation

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(
                isinstance(coord, int) and coord >= 0
                for coord in value
            )
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters, considering position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                line = (" " * self.__position[0]) + ("#" * self.__size)
                print(line)
