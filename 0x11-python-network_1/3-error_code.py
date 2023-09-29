#!/usr/bin/python3
"""
A Python script that takes in a URL,
sends a request to the URL, and displays
the body of the response (decoded in utf-8).
Manages urllib.error.HTTPError exceptions and
prints: Error code: followed by the HTTP status code.
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
        sys.exit(1)

    except urllib.error.URLError as e:
        print("Error accessing the URL:", e)
        sys.exit(1)
