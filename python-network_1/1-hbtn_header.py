#!/usr/bin/python3
"""SALAM"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        # Work in all Python versions used by Holberton sandbox
        x_request_id = response.getheader("X-Request-Id")
        print(x_request_id)
