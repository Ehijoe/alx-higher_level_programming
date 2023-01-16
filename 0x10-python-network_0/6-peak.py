#!/usr/bin/python3
"""Find a peak in a list."""


def find_peak(list_of_integers):
    """Return the peak of a list."""
    length = len(list_of_integers)
    if length == 0:
        return None
    if length == 1:
        return list_of_integers[0]
    for i in range(1, length - 1):
        a = list_of_integers[i]
        if a >= list_of_integers[i - 1] and a >= list_of_integers[i + 1]:
            return a
    if list_of_integers[1] <= list_of_integers[0]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]
    return None
