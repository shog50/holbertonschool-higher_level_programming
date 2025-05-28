#!/usr/bin/env python3
"""
VerboseList module extending Python's built-in list to provide notifications.
"""


class VerboseList(list):
    """Custom list class that provides notifications when modified."""

    def append(self, item):
        """Appends an item to the list and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list with multiple items and prints a notification."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Removes an item from the list and prints a notification."""
        if item in self:
            super().remove(item)
            print(f"Removed [{item}] from the list.")
        else:
            print(f"Item [{item}] not found in the list.")

    def pop(self, index=-1):
        """Pops an item from the list and prints a notification."""
        if self:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
            return item
        else:
            print("Cannot pop from an empty list.")


if __name__ == "__main__":

    """Testing the VerboseList class."""
    vl = VerboseList([1, 2, 3])
    vl.append(4)
