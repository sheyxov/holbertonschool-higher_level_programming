#!/usr/bin/python3
"""Salam"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value as integer and > 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
