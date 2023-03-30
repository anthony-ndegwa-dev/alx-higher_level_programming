#!/usr/bin/env bash
# Script to show the Content-Length from a HTTP request
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
