#!/usr/bin/python3
"""Replace in a copy."""


def new_in_list(my_list, idx, element):
    """Replace an element in a copy of a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
