#!/usr/bin/python3
"""Can you C me now."""


def no_c(my_string):
    """Return my_string without 'C' or 'c'."""
    new_str = ""
    for character in my_string:
        if character not in ['c', 'C']:
            new_str += character
    return new_str
