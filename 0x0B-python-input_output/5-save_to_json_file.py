#!/usr/bin/python3
"""Save Object to a file."""
import json


def save_to_json_file(my_obj, filename):
    """Write a python object to a JSON file."""
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(my_obj, json_file)
