#!/usr/bin/python3
"""List the 10 most recent commits of a github repository."""
import requests
import sys

if __name__ == '__main__':
    url = f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits"
    resp = requests.get(url, params={"per_page": "10"})
    commits = resp.json()
    for commit in commits:
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")
