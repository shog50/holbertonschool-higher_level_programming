#!/usr/bin/python3
"""
Defines a Student class with JSON serialization and deserialization.
"""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            return {
                a: self.__dict__[a]
                for a in attrs
                if isinstance(a, str) and a in self.__dict__
            }
        return self.__dict__

    def reload_from_json(self, json):
        for key in json:
            self.__dict__[key] = json[key]
