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
const url = 'https://swapi-api.alx-tools.com/api/films/';
let id = parseInt(process.argv[2], 10);
let characters = [];

request(url, function (err, response, body) {
  if (err == null) {
    const resp = JSON.parse(body);
    const results = resp.results;
    if (id < 4) {
      id += 3;
    } else {
      id -= 3;
    }
    for (let i = 0; i < results.length; i++) {
      if (results[i].episode_id === id) {
        characters = results[i].characters;
        break;
      }
    }
    for (let j = 0; j < characters.length; j++) {
      request(characters[j], function (err, response, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
