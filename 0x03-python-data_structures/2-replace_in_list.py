#!/usr/bin/python3
"""Replace element."""


def replace_in_list(my_list, idx, element):
    """Replace an element in a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
