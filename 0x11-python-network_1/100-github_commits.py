#!/usr/bin/python3
"""
A Python script that lists 10 commits
(from the most recent to oldest)
of a specified repository by a given owner using
the GitHub API.
"""

import sys
import requests

if __name__ == '__main__':
    rep_name = sys.argv[1]
    own_name = sys.argv[2]

    url_api = 'https://api.github.com/repos/{}/{}/commits'.format(
        own_name, rep_name)

    try:
        response = requests.get(url_api)
        response.raise_for_status()

        for commit in response.json()[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author_name))

    except requests.exceptions.HTTPError as e:
        print("Error code:", e.response.status_code)
        sys.exit(1)

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)
