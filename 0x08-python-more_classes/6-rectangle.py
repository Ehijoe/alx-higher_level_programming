#!/usr/bin/python3
"""Rectangle."""


class Rectangle:
    """A rectangle class."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Create a new rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Return the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the string equivalent of the rectangle."""
        rect = ""
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.height):
            for i in range(self.width):
                rect += "#"
            rect += "\n"
        return rect[:-1]

    def __repr__(self):
        """Return an official string representation of a rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Delete a rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
