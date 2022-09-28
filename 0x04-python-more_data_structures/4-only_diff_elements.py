#!/usr/bin/python3
"""Only differents."""


def only_diff_elements(set_1: set, set_2: set):
    """Return the elements that are in only one set."""
    return set_1.union(set_2) - set_1.intersection(set_2)
