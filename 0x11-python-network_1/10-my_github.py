#!/usr/bin/python3
"""A script that takes your GitHub credentials
(username and password),uses the GitHub API to display your id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username, password = sys.argv[1], sys.argv[2]
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(username, password)

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        user_data = response.json()
        user_id = user_data.get("id")
        print(user_id if response.status_code == 200 else None)

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)
