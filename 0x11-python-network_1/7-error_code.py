#!/usr/bin/python3
"""
A script that
takes in a URL as a command line argument
sends a GET request to the URL using the requests library
displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        print("Error code:", e.response.status_code)
        sys.exit(1)

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)

    print(response.text)
