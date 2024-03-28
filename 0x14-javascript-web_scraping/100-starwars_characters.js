#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
    return;
  }

  const movieData = JSON.parse(body);

  const characterPromises = movieData.characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(new Error(error));
          return;
        }

        if (response.statusCode !== 200) {
          reject(new Error(`Status: ${response.statusCode}`));
          return;
        }

        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  });

  Promise.all(characterPromises)
    .then(characterNames => {
      characterNames.forEach(name => {
        console.log(name);
      });
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
