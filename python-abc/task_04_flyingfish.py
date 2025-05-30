#!/usr/bin/env python3
"""Module that explores multiple inheritance with a FlyingFish class."""


class Fish:
    """Defines Fish behavior."""

    def swim(self):
        """Prints how the fish moves."""
        print("The fish is swimming.")

    def habitat(self):
        """Prints where the fish lives."""
        print("The fish lives in water.")


class Bird:
    """Defines Bird behavior."""

    def fly(self):
        """Prints how the bird moves."""
        print("The bird is flying.")

    def habitat(self):
        """Prints where the bird lives."""
        print("The bird lives in the sky.")


class FlyingFish(Fish, Bird):
    """FlyingFish class inherits from both Fish and Bird."""

    def fly(self):
        """Prints how the flying fish moves."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints how the flying fish moves."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints where the flying fish lives."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()

    # Print method resolution order (MRO)
    print(FlyingFish.__mro__)
