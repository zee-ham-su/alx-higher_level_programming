#!/usr/bin/node
const dict = require('./101-data.js').dict;

const userIDsByOccurrence = {};

for (const userID in dict) {
  const occurrence = dict[userID];

  if (userIDsByOccurrence[occurrence] === undefined) {
    userIDsByOccurrence[occurrence] = [];
  }

  userIDsByOccurrence[occurrence].push(userID);
}

console.log(userIDsByOccurrence);
