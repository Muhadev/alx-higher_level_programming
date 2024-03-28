#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Check if both URL and file path are provided
if (process.argv.length !== 4) {
  console.log('Usage: node 5-request_store.js <URL> <file_path>');
  process.exit(1);
}

// Extract URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    // If there's an error during the request, print it
    console.error(error);
  } else if (response.statusCode !== 200) {
    // If the request fails, print the status code
    console.error(`Failed to fetch webpage. Status code: ${response.statusCode}`);
  } else {
    // Write the body response to the file
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        // If there's an error during writing, print it
        console.error(err);
      } else {
        console.log(`Webpage content has been stored in ${filePath}`);
      }
    });
  }
});
