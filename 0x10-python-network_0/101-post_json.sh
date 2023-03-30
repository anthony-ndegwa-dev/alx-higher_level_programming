#!/usr/bin/env bash
# Script sends a JSON POST request to a URL passed as argument, and displays body of the response
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
