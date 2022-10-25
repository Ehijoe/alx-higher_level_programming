#!/usr/bin/python3
"""Write to a file."""


def write_file(filename="", text=""):
    """Write some text to a file."""
    with open(filename, "w", encoding="utf-8") as output_file:
        output_file.write(text)
