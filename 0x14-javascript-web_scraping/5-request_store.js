#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const sourceUrl = process.argv[2];
const destinationFile = process.argv[3];

request(sourceUrl, (requestError, response, body) => {
  if (requestError) {
    console.log(requestError);
  } else {
    fs.writeFile(destinationFile, body, 'utf8', (writeError) => {
      if (writeError) {
        console.log(writeError);
      }
    });
  }
});
