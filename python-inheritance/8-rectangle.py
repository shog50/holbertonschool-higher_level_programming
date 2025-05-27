#!/usr/bin/python3
"""
Rectangle module inheriting from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle with validated width and height"""

    def __init__(self, width, height):
        """Initializes a Rectangle instance after validation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
