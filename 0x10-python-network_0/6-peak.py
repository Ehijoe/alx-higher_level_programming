#!/usr/bin/python3
"""Find a peak in a list."""


def find_peak(list_of_integers):
    """Return the peak of a list."""
    length = len(list_of_integers)
    if length == 0:
        return None
    if length == 1:
        return list_of_integers[0]
    if length == 2:
        return max(*list_of_integers)
    mid = (length + 1) // 2
    mid_num = list_of_integers[mid]
    if mid - 1 > 0 and mid_num < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    elif mid + 1 < length and mid_num < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid + 1:])
    else:
        return mid_num
