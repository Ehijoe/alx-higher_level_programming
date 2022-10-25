#!/usr/bin/python3
"""Read file."""


def read_file(filename=""):
    """Print the contents of a file to stdout."""
    with open(filename, "r", encoding="utf-8") as file_:
        print(file_.read())
