#!/usr/bin/python3
"""Delete by value."""


def complex_delete(a_dictionary, value):
    """Delete a key with a specified value from a dictionary."""
    for key in a_dictionary:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
