#!/usr/bin/env python3
"""
Basic Serialization module:
- serialize_and_save_to_file(data, filename):
  Serializes a Python dictionary to a JSON file (overwrites if exists).
- load_and_deserialize(filename):
  Loads JSON data from a file and returns it as a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it as a JSON file.

    Args:
        data (dict): The data to serialize.
        filename (str): The output file path.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a Python dictionary.

    Args:
        filename (str): The JSON file path to read from.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
