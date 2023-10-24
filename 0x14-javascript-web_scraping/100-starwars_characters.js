#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node starWarsCharacters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    if (characters.length === 0) {
      console.log('No characters found for this movie.');
    } else {
      characters.forEach((characterUrl) => {
        request(characterUrl, function (charError, charResponse, charBody) {
          if (!charError && charResponse.statusCode === 200) {
            const character = JSON.parse(charBody);
            console.log(character.name);
          } else {
            console.error('Error fetching character:', charError);
          }
        });
      });
    }
  } else {
    console.error('An error occurred. Status code:', response.statusCode);
  }
});
