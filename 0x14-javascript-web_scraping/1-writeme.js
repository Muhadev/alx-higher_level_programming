#!/usr/bin/node
const fs = require('fs');

// Check if both file path and string to write are provided
if (process.argv.length < 4) {
  console.log('Usage: node 1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

// Extract file path and string to write from command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    // Print the error object if an error occurred during writing
    console.error(err);
  }
});
