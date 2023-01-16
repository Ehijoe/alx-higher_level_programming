#!/bin/bash
# Send a post request with data from a json file
curl -s -H "Content-Type: application/json" -d "@$2" "$1"
