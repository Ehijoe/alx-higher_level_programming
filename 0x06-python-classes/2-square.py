#!/usr/bin/python3
"""My first square."""


class Square:
    """An empty square class."""

    def __init__(self, size=0):
        """Create a square of a particular size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
