#!/usr/bin/python3
"""Multiply by 2."""


def multiply_by_2(a_dictionary):
    """Double the values in a dictionary."""
    return {key: a_dictionary[key] * 2 for key in a_dictionary}
