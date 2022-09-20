#!/usr/bin/python3
"""Function to remove a character from a string."""


def remove_char_at(str, n):
    """Remove a character from a string."""
    ans = ""
    for i, c in enumerate(str):
        if i != n:
            ans += c
    return ans
