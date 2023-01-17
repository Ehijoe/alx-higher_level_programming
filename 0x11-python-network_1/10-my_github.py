#!/usr/bin/python3
"""Use the github API."""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == '__main__':
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    resp = requests.get("https://api.github.com/user",
                        headers=headers, auth=auth)
    user = resp.json()
    print(user.get('id'))
