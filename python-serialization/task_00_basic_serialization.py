#!/usr/bin/env python3
"""Basic JSON serialization and deserialization module"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a dictionary to JSON and save to a file.
    If the file exists, overwrite it.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it into a dictionary.
    Returns the Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
