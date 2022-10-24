#!/usr/bin/python3
"""Geometry module."""


class BaseGeometry:
    """Baseclass for all shapes."""

    def area(self):
        """Return the area of the shape."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A rectangle."""

    def __init__(self, width, height):
        """Create a rectangle."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
