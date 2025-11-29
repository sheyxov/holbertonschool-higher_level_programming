#!/usr/bin/python3
"""Defines a Student class with JSON serialization/deserialization."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary representation of the Student instance.
        If attrs is a list of strings, return only attribute names
        contained in this list.
        """
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            return {
                key: self.__dict__[key]
                for key in attrs if key in self.__dict__
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using the
        key/value pairs from the dictionary json.
        """
        for key, value in json.items():
            setattr(self, key, value)
