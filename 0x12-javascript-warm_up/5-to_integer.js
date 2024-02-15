#!/usr/bin/node

const argument = process.argv[2];
const num = parseInt(argument);

if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
