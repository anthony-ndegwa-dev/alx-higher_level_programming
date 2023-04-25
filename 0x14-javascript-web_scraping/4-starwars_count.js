#!/usr/bin/node
/**
 * Script that prints the number of movies where the character
 * “Wedge Antilles” is present
 * The first argument is the API URL of the Star wars API:
 *  https://swapi-api.alx-tools.com/api/films/
 * Wedge Antilles is character ID 18 - your script must use this
 *  ID for filtering the result of the API
 * You must use the module request
 */
const request = require('request');
let numFilms = 0;

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const resp = JSON.parse(body);
    const results = resp.results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          numFilms++;
        }
      }
    }
  }
  console.log(numFilms);
});
