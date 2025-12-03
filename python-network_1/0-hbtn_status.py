#!/usr/bin/python3
"""Fetches a URL using urllib and prints the response body."""
import urllib.request


def fetch_status():
    """Fetches intranet status page and prints details."""
    url = "https://intranet.hbtn.io/status"
    headers = {"cfclearance": "true"}

    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as response:
        body = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    fetch_status()
