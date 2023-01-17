#!/usr/bin/python3
"""Handle errors."""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
import sys

if __name__ == '__main__':
    req = Request(sys.argv[1])
    try:
        with urlopen(req) as resp:
            print(resp.read().decode("utf-8"))
    except HTTPError as err:
        print(f"Error code: {err.code}")
