#!/usr/bin/python3
"""Search for a name using an api."""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    resp = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        user = resp.json()
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
    if type(user) is not dict or "id" not in user or "name" not in user:
        print("No result")
    else:
        print(f"[{user['id']}] {user['name']}")
