#!/usr/bin/python3
"""List the 10 most recent commits of a github repository."""
import requests
import sys

if __name__ == '__main__':
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    resp = requests.get(url, params={"per_page": "10"}, headers=headers)
    commits = resp.json()
    for commit in commits:
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")
