#!/usr/bin/python3
"""Simple delete by key."""


def simple_delete(a_dictionary, key=""):
    """Delete a key-value pair from a dictionary."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
