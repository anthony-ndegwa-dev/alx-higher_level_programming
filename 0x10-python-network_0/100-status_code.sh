#!/usr/bin/env bash
# Script to send request to URL passed as an argument, and display status code of the response
curl -so /dev/null -w "%{http_code}" "$1"
