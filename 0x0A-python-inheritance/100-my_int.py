#!/usr/bin/python3
"""Custom integers."""


class MyInt(int):
    """A custom integer class."""

    def __ne__(self, x):
        """Return True if x is equal to self."""
        return int(self) == x

    def __eq__(self, x):
        """Return True if x is not equal to self."""
        return int(self) != x
