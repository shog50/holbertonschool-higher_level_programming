#!/usr/bin/python3
"""
Defines a Student class with attributes and JSON serialization.
"""


class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the Student instance."""
        return self.__dict__
