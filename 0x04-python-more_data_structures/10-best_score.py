#!/usr/bin/python3
"""Best score."""


def best_score(a_dictionary):
    """Return the key with the biggest number in a dictionary."""
    if a_dictionary is None:
        return None
    best = None
    maximum = None
    for key in a_dictionary:
        if maximum is None or maximum < a_dictionary[key]:
            best = key
            maximum = a_dictionary[key]
    return best
