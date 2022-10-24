#!/usr/bin/python3
"""Add attribute."""


def add_attribute(obj, key, val):
    """Add an attribute to an object or raises an exception."""
    if "__dict__" in dir(obj):
        setattr(obj, key, val)
    else:
        raise TypeError("can't add new attribute")
