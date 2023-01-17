#!/usr/bin/python3
"""Send data with a request."""
import requests
import sys

if __name__ == '__main__':
    data = {"email": sys.argv[2]}
    resp = requests.post(sys.argv[1], data=data)
    print(resp.text)
