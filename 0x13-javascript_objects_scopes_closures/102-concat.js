#!/usr/bin/node

const fs = require('fs');

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

const content1 = fs.readFileSync(sourceFilePath1, 'utf-8');
const content2 = fs.readFileSync(sourceFilePath2, 'utf-8');

const concatenatedContent = content1 +  content2;

fs.writeFileSync(destinationFilePath, concatenatedContent);

console.log(`Files ${sourceFilePath1} and ${sourceFilePath2} successfully concatenated to ${destinationFilePath}`);
