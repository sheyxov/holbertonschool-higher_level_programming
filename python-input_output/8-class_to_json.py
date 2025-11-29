#!/usr/bin/python3
"""Defines a function that returns the dictionary description of an object."""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.
    Only attributes that are basic Python types are included.
    """
    return obj.__dict__
