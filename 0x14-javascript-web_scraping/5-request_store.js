#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error === null) {
    fs.writeFileSync(filePath, body, 'utf-8');
    console.log(`Successfully saved the content from ${url} to ${filePath}`);
  }
});
