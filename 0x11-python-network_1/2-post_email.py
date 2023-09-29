#!/usr/bin/python3
"""
A Python script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""


if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    try:
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')
        with urllib.request.urlopen(url, data=data) as response:
            html = response.read().decode('utf-8')
            print(html)

    except urllib.error.URLError as e:
        print("Error accessing the URL:", e)
        sys.exit(1)
