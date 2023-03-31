#!/usr/bin/python3
"""
Script takes in URL, sends a request to it & displays body of the response.

    If HTTP status code is >= 400, print: Error code: followed by the value of
       HTTP status code
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to check arguments passed to the script (number or type)
"""
import sys
import requests


if __name__ == '__main__':
    request = requests.get(sys.argv[1])
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
