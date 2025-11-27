#!/usr/bin/python3
"""Salam"""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly an instance of the specified class ; otherwise False."""
    if not isinstance(obj, a_class):
        return False
    else:
        return True
