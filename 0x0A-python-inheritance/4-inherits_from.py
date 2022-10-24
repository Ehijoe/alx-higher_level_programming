#!/usr/bin/python3
"""Only subclass of."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class."""
    cls = obj.__class__
    return cls is not a_class and issubclass(cls, a_class)
