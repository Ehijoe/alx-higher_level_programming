#!/usr/bin/python3
"""Student to JSON."""


class Student:
    """A student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the JSON representation of the student."""
        if type(attrs) is list and all([type(i) is str for i in attrs]):
            return {att: self.__dict__[att]
                    for att in self.__dict__
                    if att in attrs}
        return dict(self.__dict__)
