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

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Make a request to the Star Wars API to get the movie data
request(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
    return;
  }

  // Parse the JSON response body into an object
  const movieData = JSON.parse(body);

  // Print all character names in the same order as the list "characters" in the response
  movieData.characters.forEach((characterUrl) => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }
      if (response.statusCode !== 200) {
        console.error(`Request failed with status code ${response.statusCode}`);
        return;
      }

      // Parse the JSON response body into an object
      const characterData = JSON.parse(body);

      // Print the character name
      console.log(characterData.name);
    });
  });
});
