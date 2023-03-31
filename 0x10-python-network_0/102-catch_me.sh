#!/bin/bash
# Script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond You got me!.
curl -s -L  -X PUT  -H 'Origin: School' localhost:5000/catch_me_3
