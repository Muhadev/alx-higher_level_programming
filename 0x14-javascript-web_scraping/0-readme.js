#!/usr/bin/node
const fs = require('fs');

// Extract file path from command line argument
const filePath = process.argv[2];

// Read the content of the file
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Print the error object if an error occurred during reading
    console.error(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
