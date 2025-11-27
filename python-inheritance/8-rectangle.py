#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize Rectangle with validated width and height"""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """String representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
