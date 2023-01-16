#!/bin/bash
# Send a post request with parameters
curl -s -X "POST" -d "email=test%40gmail.com&subject=I+will+always+be+here+for+PLD" "$1"
