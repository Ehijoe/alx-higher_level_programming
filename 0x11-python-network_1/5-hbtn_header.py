#!/usr/bin/python3
"""Get the Request ID from the header of a response."""
import requests
import sys

if __name__ == '__main__':
    resp = requests.get(sys.argv[1])
    print(resp.headers['X-Request-Id'])
