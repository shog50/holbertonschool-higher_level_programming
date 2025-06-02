"""
This module contains the function `save_to_json_file` that
writes an object to a text file using its JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file in JSON format.

    Args:
        my_obj: The object to serialize to JSON.
        filename: The name of the file to write to.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
