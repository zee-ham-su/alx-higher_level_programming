#!/bin/bash
# Post JSON file and display response.
[ -f "$2" ] && curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1"
