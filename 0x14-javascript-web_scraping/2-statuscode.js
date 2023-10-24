#!/usr/bin/node

const request = require('request');
const targetURL = process.argv[2];

request(targetURL, function (error, httpResponse) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + httpResponse.statusCode);
  }
});
