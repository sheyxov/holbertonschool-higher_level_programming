#!/usr/bin/python3
"""
This module defines the MyList class.
The MyList class inherits from the built-in list type and
provides a method to print a sorted version of the list
without modifying the original order of elements.
"""


class MyList(list):
    """
    A custom list class that inherits from list
    and provides a method to print the list sorted.
    """
    def print_sorted(self):
        """ prints the list, but sorted """
        new_list = sorted(self)
        print(new_list)

