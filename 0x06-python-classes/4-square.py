#!/usr/bin/python3
"""My first square."""


class Square:
    """An empty square class."""

    def __init__(self, size=0):
        """Create a square of a particular size."""
        self.size = size

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, val):
        """Set the size of the square."""
        if type(val) is not int:
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    def area(self):
        """Return the area of the square."""
        return (self.__size ** 2)
