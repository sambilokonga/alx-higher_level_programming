#!/usr/bin/python3
"""
Get the 10 most recent commits of the passed in repository
of a given user, then display the sha and author name
It's... apparently a Holberton School interview question
"""
import requests
import sys


def get_commits():
    req = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(sys.argv[2], sys.argv[1]))

    for recent_commit in req.json()[:10]:
        print("{}: {}".format(recent_commit.get('sha'),
                              recent_commit.get('commit')
                              .get('author').get('name')))


if __name__ == '__main__':
    get_commits()
