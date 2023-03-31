#!/usr/bin/python3
"""
Script takes in URL, sends request to URL & displays value of
X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        page = response.info()
        print(page.get('X-Request-Id'))
