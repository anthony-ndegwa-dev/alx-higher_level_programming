#!/bin/bash
# Script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond You got me!.
curl -s -X PUT -H "Content-Type: application/json" -d '{"message": "You got me!"}' 0.0.0.0:5000/catch_me
