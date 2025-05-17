#!/usr/bin/python3
"""
This module defines the function `text_indentation`
which prints a text with two new lines after '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): The input text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    for i, char in enumerate(text):
        if char in ".?:":
            print(text[start:i + 1].strip())
            print()
            start = i + 1
    if start < len(text):
        print(text[start:].strip(), end="")
