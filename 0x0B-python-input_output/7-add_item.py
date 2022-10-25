#!/usr/bin/python3
"""Load, add, save."""
import sys


save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


def main():
    """Return the exit status of the program."""
    if len(sys.argv) <= 1:
        return 0
    try:
        old = load("add_item.json")
    except FileNotFoundError:
        old = []
    old += sys.argv[1:]
    save(old, "add_item.json")


if __name__ == '__main__':
    sys.exit(main())
