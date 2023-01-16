#!/bin/bash
# Display the body size of a request
curl -sI "$1" | grep -i "Content-Length: " | cut --delimiter=" " -f 2-
