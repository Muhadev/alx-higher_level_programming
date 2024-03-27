#!/usr/bin/node
const request = require('request');

// Check if API URL is provided
if (process.argv.length !== 3) {
  console.log('Usage: node 4-starwars_count.js <API_URL>');
  process.exit(1);
}

// Extract API URL from command line argument
const apiUrl = process.argv[2];

// Make a GET request to the Star Wars API films endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // If there's an error during the request, print it
    console.error(error);
  } else if (response.statusCode !== 200) {
    // If the request fails, print the status code
    console.error(`Failed to fetch films. Status code: ${response.statusCode}`);
  } else {
    // Parse the JSON response
    const filmsData = JSON.parse(body);

    // Count the number of films where Wedge Antilles is present
    const count = filmsData.results.reduce((total, film) => {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        return total + 1;
      }
      return total;
    }, 0);

    // Print the count
    console.log(count);
  }
});
