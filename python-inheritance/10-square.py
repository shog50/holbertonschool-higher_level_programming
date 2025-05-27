#!/usr/bin/python3
"""
Square module inheriting from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square, inheriting from Rectangle"""

    def __init__(self, size):
        """Initializes a Square instance after validation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)  # Calls Rectangle with equal width and height
