#!/usr/bin/python3
"""
A Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
import sys

if __name__ == '__main__':
    target_url = 'http://0.0.0.0:5000/search_user'

    search_letter = sys.argv[1] if len(sys.argv) > 1 else ""

    request_payload = {'q': search_letter}

    try:
        response = requests.post(target_url, data=request_payload)
        try:
            json_data = response.json()
        except ValueError:
            print("Not a valid JSON")
            sys.exit(1)

        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)
