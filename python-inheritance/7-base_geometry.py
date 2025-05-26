#!/usr/bin/python3
"""
This module defines a class BaseGeometry with validation methods.
"""


class BaseGeometry:
    """A class representing geometric shapes with validation methods."""

    def area(self):
        """Raises an exception because area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:  # Ensuring strict type checking
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:  # Ensuring proper validation
            raise ValueError("{} must be greater than 0".format(name))
