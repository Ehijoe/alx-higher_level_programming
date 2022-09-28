#!/usr/bin/python3
"""Search and replace."""


def search_replace(my_list, search, replace):
    """Replace all occurrences of an element in a list."""
    if my_list is None:
        return []
    return [num if num != search else replace for num in my_list]
