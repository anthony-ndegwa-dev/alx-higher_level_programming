#!/bin/bash
# Script takes in URL, sends a GET request to the URL,
# and displays the body of the response.
# Display only body of a 200 status code response
curl -Ls "$1"
