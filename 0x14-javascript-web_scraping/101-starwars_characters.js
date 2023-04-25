#!/usr/bin/node
/**
 * A script that prints all characters of a Star Wars movie:
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line in the same order of the list
 *  “characters” in the /films/ response
 * You must use the Star wars API
 * You must use the module request
 */
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Unexpected status code: ${response.statusCode}`);
  } else {
    const movie = JSON.parse(body);
    movie.characters.forEach((characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.error(error);
        } else if (response.statusCode !== 200) {
          console.error(`Unexpected status code: ${response.statusCode}`);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
