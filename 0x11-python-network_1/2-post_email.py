#!/usr/bin/python3
"""Send data with a request."""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import sys

if __name__ == '__main__':
    data = urlencode({"email": sys.argv[2]}).encode("ascii")
    req = Request(sys.argv[1], data=data)
    with urlopen(req) as resp:
        print(resp.read().decode("utf-8"))
