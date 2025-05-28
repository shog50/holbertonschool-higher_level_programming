#!/usr/bin/env python3
"""
Shape module using Abstract Base Classes (ABC) and duck typing
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class representing a Shape"""

    @abstractmethod
    def area(self):
        """Abstract method to compute the area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to compute the perimeter"""
        pass


class Circle(Shape):
    """Circle subclass inheriting from Shape"""

    def __init__(self, radius):
        """Initializes a Circle instance"""
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        """Computes and returns the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Computes and returns the perimeter of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle subclass inheriting from Shape"""

    def __init__(self, width, height):
        """Initializes a Rectangle instance"""
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def area(self):
        """Computes and returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Computes and returns the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a shape using duck typing"""
    try:
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")
    except AttributeError:
        print("Error: Provided object does not implement the required methods")


if __name__ == "__main__":
    """Testing the implementation"""
    try:
        circle = Circle(radius=5)
        rectangle = Rectangle(width=4, height=7)

        shape_info(circle)
        shape_info(rectangle)
    except ValueError as e:
        print(f"Initialization Error: {e}")

