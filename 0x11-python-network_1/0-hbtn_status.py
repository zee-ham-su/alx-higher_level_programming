#!/usr/bin/python3
""" a Python script that fetches
https://alx-intranet.hbtn.io/status
"""


if __name__ == '__main__':
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        html = response.read()
        decoded_html = html.decode('utf-8')
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", decoded_html)
