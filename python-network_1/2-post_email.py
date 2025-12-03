#!/usr/bin/python3
"""Sends POST request with an email parameter and prints the response body."""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode POST data
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    # Build request object (POST because data is provided)
    req = urllib.request.Request(url, data=data)

    # Send request and read response
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
