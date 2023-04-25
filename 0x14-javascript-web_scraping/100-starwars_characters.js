#!/usr/bin/node
/**
 * A script that prints all characters of a Star Wars movie:
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line
 * You must use the Star wars API
 * You must use the module request
 */
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (err, response, body) {
  if (err == null) {
    const resp = JSON.parse(body);
    const characters = resp.characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (err, response, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
