#!/usr/bin/node
const request = require('request');

// Check if movie ID is provided
if (process.argv.length !== 3) {
  console.log('Usage: node 3-starwars_title.js <movie_ID>');
  process.exit(1);
}

// Extract movie ID from command line argument
const movieID = process.argv[2];

// Make a GET request to the Star Wars API
request.get(`https://swapi-api.alx-tools.com/api/films/${movieID}`, (error, response, body) => {
  if (error) {
    // If there's an error during the request, print it
    console.error(error);
  } else if (response.statusCode !== 200) {
    // If the request fails, print the status code
    console.error(`Failed to fetch movie. Status code: ${response.statusCode}`);
  } else {
    // Parse the JSON response
    const movieData = JSON.parse(body);
    // Print the title of the movie
    console.log(movieData.title);
  }
});
