#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.

    Args:
        my_obj (any): The Python object to serialize.
        filename (str): The file name to write to.

    Usage example:

    >>> import os
    >>> filename = "test.json"
    >>> my_obj = {"name": "Alice", "age": 30}
    >>> save_to_json_file(my_obj, filename)
    >>> with open(filename, "r") as f:
    ...     content = f.read()
    >>> print(content)
    {"name": "Alice", "age": 30}
    >>> os.remove(filename)
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
