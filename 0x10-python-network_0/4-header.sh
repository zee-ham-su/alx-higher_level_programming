#!/bin/bash
#send GET request with specific header, and displays the response body
curl -s -H "X-School-User-Id: 98" "$1"
