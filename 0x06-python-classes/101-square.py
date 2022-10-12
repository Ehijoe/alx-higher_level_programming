#!/usr/bin/python3
"""My first square."""


class Square:
    """An empty square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Create a square of a particular size."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @property
    def position(self):
        """Return the position of the square."""
        return self.__position

    @size.setter
    def size(self, val):
        """Set the size of the square."""
        if type(val) is not int:
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    @position.setter
    def position(self, pos):
        """Set the position of the square."""
        for check in [
                "type(pos) is tuple",
                "len(pos) == 2",
                "type(pos[0]) is int",
                "type(pos[1]) is int",
                "pos[0] >= 0",
                "pos[1] >= 0",
        ]:
            if not eval(check):
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = pos

    def area(self):
        """Return the area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square in #'s."""
        print(self)

    def __repr__(self):
        """Return the string representation of a square."""
        if self.size == 0:
            return "\n"
        result = ""
        for i in range(self.position[1]):
            result += "\n"
        for i in range(self.size):
            result += (" " * self.position[0]) + ("#" * self.size)
            if i != self.size - 1:
                result += "\n"
        return result
