#!/usr/bin/python3
"""Check if a character is lowercase."""


def islower(c):
    """Check if a character is lowercase."""
    return (ord(c) >= ord('a') and ord(c) <= ord('z'))
