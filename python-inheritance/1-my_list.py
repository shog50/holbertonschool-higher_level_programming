#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""

class MyList(list):
    """A subclass of list with an additional print_sorted method."""
    
    def print_sorted(self):
        """Prints the list in ascending order without modifying the original list."""
        print(sorted(self))
