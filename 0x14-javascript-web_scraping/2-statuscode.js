#!/usr/bin/node
const request = require('request');

// Extract URL from command line argument
const url = process.argv[2];

// Make a GET request to the URL
request.get(url, (error, response) => {
  if (error) {
    // If there's an error during the request, print it
    console.error(error);
  } else {
    // Print the status code
    console.log(`code: ${response.statusCode}`);
  }
});
