#!/usr/bin/python3
"""Print sorted dictionary."""


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary."""
    for key in sorted(list(a_dictionary)):
        print(f"{key}: {a_dictionary[key]}")
