#!/usr/bin/python3
"""Append to a file."""


def append_write(filename="", text=""):
    """Append some text to a file."""
    with open(filename, "a", encoding="utf-8") as file_:
        written = file_.write(text)
        return written
    return 0
