#!/usr/bin/python3
"""Exact same object."""


def is_same_class(obj, a_class):
    """Return True only if obj is an instance of a_class."""
    return obj.__class__ is a_class
