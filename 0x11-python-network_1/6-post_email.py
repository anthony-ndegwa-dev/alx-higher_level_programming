#!/usr/bin/python3
"""
Script takes in URL and an email address, sends a POST request to the passed
URL with the email as a parameter, & finally displays body of the response.

    The email must be sent in the variable email
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    No need to error check arguments passed to the script (number or type)
"""
import sys
import requests


if __name__ == '__main__':
    request = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(request.text)
