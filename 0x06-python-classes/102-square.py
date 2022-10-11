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

    def __eq__(self, o):
        """Check if two squares are equal."""
        if type(o) is not Square:
            raise TypeError
        return self.area() == o.area()

    def __lt__(self, o):
        """Check if a square is less than another square."""
        if type(o) is not Square:
            raise TypeError
        return self.area() < o.area()

    def __gt__(self, o):
        """Check if a square is greater than another square."""
        if type(o) is not Square:
            raise TypeError
        return self.area() > o.area()

    def __ne__(self, o):
        """Check if a square is not equal to another square."""
        if type(o) is not Square:
            raise TypeError
        return self.area() != o.area()

    def __ge__(self, o):
        """Check if a square is greater than or equal to another square."""
        if type(o) is not Square:
            raise TypeError
        return self.area() >= o.area()

    def __le__(self, o):
        """Check if a square is less than or equal to another square."""
        if type(o) is not Square:
            raise TypeError
        return self.area() <= o.area()
