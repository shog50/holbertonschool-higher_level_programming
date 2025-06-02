#!/usr/bin/python3
import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): A JSON string.

    Returns:
        The Python data structure (dict, list, etc.)
        represented by the JSON string.

    Note:
        No exception handling is needed if the string is not a valid JSON.
    """
    return json.loads(my_str)
