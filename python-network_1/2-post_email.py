#!/usr/bin/python3
import sys
import urllib.request
import urllib.parse
"""SALAM"""



if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]


    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    req = urllib.request.Request(url. data=data)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode("utf-8")
        print(body)
