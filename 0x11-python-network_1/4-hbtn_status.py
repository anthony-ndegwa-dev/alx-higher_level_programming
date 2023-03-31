#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status

    You must use the package requests
    You are not allow to import packages other than requests
    The body of the response must be display like the following example
    (tabulation before -)
"""
import requests


if __name__ == '__main__':
    r = requests.get('https://alx-intranet.hbtn.io/status')
    b = r.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(b), b))
