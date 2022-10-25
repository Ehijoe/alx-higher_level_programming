#!/usr/bin/python3
"""Class to JSON."""


def class_to_json(obj):
    """Return a dictionary description of an object."""
    return dict(obj.__dict__)
