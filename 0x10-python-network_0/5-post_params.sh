#!/bin/bash
#sends POST request with specific vars, and displays the response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
