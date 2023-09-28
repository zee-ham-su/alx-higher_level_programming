#!/bin/bash
# Bash script to fetch a URL and display response body size
curl -s "$1" | wc -c


