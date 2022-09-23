#!/usr/bin/python3
"""Only by 2."""


def divisible_by_2(my_list=[]):
    """Check whether each element is even."""
    return [num % 2 == 0 for num in my_list]
