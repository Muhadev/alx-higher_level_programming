#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
if (args.length < 2) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b - a);

  const secondBiggest = sortedArgs[1];

  console.log(secondBiggest);
}
