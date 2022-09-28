#!/usr/bin/python3
"""Weighted average."""


def weight_average(my_list=[]):
    """Return the weighted average given a list of the weights and scores."""
    return sum([a[0] * a[1] for a in my_list]) / sum(a[0] for a in my_list)
