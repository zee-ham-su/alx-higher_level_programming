#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let characterCount = 0;

    for (const filmIdx in films) {
      const charactersInFilm = films[filmIdx].characters;

      for (const charIdx in charactersInFilm) {
        if (charactersInFilm[charIdx].includes('18')) {
          characterCount++;
        }
      }
    }

    console.log(characterCount);
  } else {
    console.error('An error occurred. Status code: ' + response.statusCode);
  }
});
