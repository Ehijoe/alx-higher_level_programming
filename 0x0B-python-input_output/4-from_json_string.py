#!/usr/bin/python3
"""From JSON string to Object."""
import json


def from_json_string(my_str):
    """Convert a JSON string to a python object."""
    return json.loads(my_str)
