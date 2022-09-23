#!/usr/bin/python3
"""Delete at."""


def delete_at(my_list=[], idx=0):
    """Delete an element from a list given its index."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
