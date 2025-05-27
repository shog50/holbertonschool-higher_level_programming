#!/usr/bin/env python3
"""
Animal module using Abstract Base Classes (ABC)
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an Animal"""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses"""
        pass


class Dog(Animal):
    """Dog subclass inheriting from Animal"""

    def sound(self):
        """Returns the sound a dog makes"""
        return "Bark"


class Cat(Animal):
    """Cat subclass inheriting from Animal"""

    def sound(self):
        """Returns the sound a cat makes"""
        return "Meow"
