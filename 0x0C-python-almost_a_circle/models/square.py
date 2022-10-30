#!/usr/bin/python3
"""A square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of a square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self):
        """Return the size of the square."""
        return self.width

    @size.setter
    def size(self, size):
        """Set the size of a square."""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the rectangle according to the arguments."""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        if len(args) == 0:
            for key in kwargs:
                if key in ["id", "size", "x", "y"]:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Reperesent a rectangle as a dictionary."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
