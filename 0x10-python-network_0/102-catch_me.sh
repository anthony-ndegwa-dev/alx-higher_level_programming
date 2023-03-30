#!/usr/bin/env bash
# Script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond You got me!.
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "You got me!"
