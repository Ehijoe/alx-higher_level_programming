#!/usr/bin/python3
"""Geometry module."""


class BaseGeometry:
    """Baseclass for all shapes."""

    def area(self):
        """Return the area of the shape."""
        raise Exception("area() is not implemented")
