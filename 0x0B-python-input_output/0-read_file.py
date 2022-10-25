#!/usr/bin/python3
"""Read file."""


def read_file(filename=""):
    """Print the contents of a file to stdout."""
    with open(filename) as file_:
        print(file_.read())
