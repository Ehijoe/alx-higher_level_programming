#!/usr/bin/python3
"""Lookup."""


def lookup(obj):
    """Return a list of the attributes of obj."""
    return list(vars(obj))
