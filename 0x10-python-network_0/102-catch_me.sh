#!/bin/bash
# Script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond You got me!.
curl 0.0.0.0:5000/catch_me -sLX PUT -d "user_id=98" -H "Origin: You got me!"
