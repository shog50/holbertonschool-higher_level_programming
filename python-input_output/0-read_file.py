#!/usr/bin/python3
"""
This module provides a function to read and print the contents of a text file.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its contents to stdout.

    Args:
        filename (str): The path to the text file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
