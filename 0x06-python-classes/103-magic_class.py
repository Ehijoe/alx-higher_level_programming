#!/usr/bin/python3
"""The magical class."""
import math
import dis


class MagicClass:
    """A magic circle."""

    def __init__(self, radius=0):
        """Create a magical circle."""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius


if __name__ == '__main__':
    dis.dis(MagicClass)
