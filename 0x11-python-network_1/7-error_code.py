#!/usr/bin/python3
"""Handle errors."""
import requests
import sys

if __name__ == '__main__':
    resp = requests.get(sys.argv[1])
    if resp.status_code >= 400:
        print(f"Error code: {resp.status_code}")
    else:
        print(resp.text)
