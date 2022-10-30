#!/usr/bin/python3
"""The Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def update(self, *args, **kwargs):
        """Update the rectangle according to the arguments."""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
        if len(args) == 0:
            for key in kwargs:
                if key in ["id", "width", "height", "x", "y"]:
                    setattr(self, key, kwargs[key])

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display a rectangle using #'s."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def to_dictionary(self):
        """Reperesent a rectangle as a dictionary."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

    def __str__(self):
        """Return the string representation of a rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    @property
    def width(self):
        """Get the width property."""
        return self.__width

    @property
    def height(self):
        """Get the height property."""
        return self.__height

    @property
    def x(self):
        """Get the x property."""
        return self.__x

    @property
    def y(self):
        """Get the y property."""
        return self.__y

    @width.setter
    def width(self, width):
        """Set the width property."""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Set the height property."""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """Set the x property."""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """Set the y property."""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
