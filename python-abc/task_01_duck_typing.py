#!/usr/bin/env python3
"""
This module defines an abstract base class 'Shape' and its subclasses
'Circle' and 'Rectangle'. It also includes a function 'shape_info'
that demonstrates duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    @abstractmethod
    def area(self) -> float:
        """Compute the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Compute the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle."""

    def __init__(self, radius: float):
        """
        Initialize a Circle.

        Args:
            radius (float): The radius of the circle.

        Raises:
            ValueError: If radius is not greater than 0.
        """
        if radius <= 0:
            raise ValueError("radius must be greater than 0")
        self.radius = radius

    def area(self) -> float:
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a rectangle."""

    def __init__(self, width: float, height: float):
        """
        Initialize a Rectangle.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.

        Raises:
            ValueError: If width or height is not greater than 0.
        """
        if width <= 0:
            raise ValueError("width must be greater than 0")
        if height <= 0:
            raise ValueError("height must be greater than 0")
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape: Shape) -> None:
    """
    Print the area and perimeter of a shape using duck typing.

    Args:
        shape (Shape): An object that implements area and perimeter.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
