#!/usr/bin/python3
"""Create object from a JSON file."""
import json


def load_from_json_file(filename):
    """Load a python object from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file_:
        return json.load(file_)
