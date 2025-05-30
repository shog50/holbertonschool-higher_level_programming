#!/usr/bin/env python3
"""Module demonstrating mixins with a Dragon class."""


class SwimMixin:
    """Mixin providing swimming ability."""

    def swim(self):
        """Prints the swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying ability."""

    def fly(self):
        """Prints the flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class inheriting from SwimMixin and FlyMixin."""

    def roar(self):
        """Prints the dragon's roar."""
        print("The dragon roars!")


if __name__ == "__main__":
    draco = Dragon()
    draco.swim()  # Outputs: The creature swims!
    draco.fly()   # Outputs: The creature flies!
    draco.roar()  # Outputs: The dragon roars!
