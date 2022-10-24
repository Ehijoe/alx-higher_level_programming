#!/usr/bin/python3
"""My list."""


class MyList(list):
    """A list that can print itself sorted."""

    def print_sorted(self):
        """Print the list sorted."""
        print(sorted(self))
