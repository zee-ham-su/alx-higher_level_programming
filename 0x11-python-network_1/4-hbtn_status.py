#!/usr/bin/python3
"""
A Python script that fetches
https://alx-intranet.hbtn.io/status
using the requests package.
"""

import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        response = requests.get(url)
        response.raise_for_status()

        content = response.text

        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)

    except requests.exceptions.RequestException as e:
        print("Error:", e)
