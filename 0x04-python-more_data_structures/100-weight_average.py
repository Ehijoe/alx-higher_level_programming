#!/usr/bin/python3
"""Weighted average."""


def weight_average(my_list=[]):
    """Return the weighted average given a list of the weights and scores."""
    if len(my_list) == 0:
        return 0
    return sum([a[0] * a[1] for a in my_list]) / sum(a[1] for a in my_list)
