#!/usr/bin/node

const request = require('request');
const apiUrl = 'https://swapi.dev/api/films/' + process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  if (index < characters.length) {
    request(characters[index], function (charError, charResponse, charBody) {
      if (!charError) {
        console.log(JSON.parse(charBody).name);
        printCharacters(characters, index + 1);
      } else {
        console.error('Error fetching character:', charError);
      }
    });
  }
}
