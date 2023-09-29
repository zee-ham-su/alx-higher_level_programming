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
        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data.get("id")
            print(user_id)
        elif response.status_code == 401:
            print("None")
        else:
            print(f"Error: {response.status_code} Client Error")
            response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)
