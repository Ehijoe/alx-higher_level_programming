#!/usr/bin/python3
"""Find the max."""


def max_integer(my_list=[]):
    """Return the biggest integer in a list."""
    if len(my_list) == 0:
        return None
    max_ = my_list[0]
    for num in my_list[1:]:
        if num > max_:
            max_ = num
    return max_
