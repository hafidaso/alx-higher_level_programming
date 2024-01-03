#!/usr/bin/node

const request = require('request');

let requestUrl = 'https://swapi-api.alx-tools.com/api/films/';
requestUrl += process.argv[2];

request(requestUrl, (err, response, body) => {
  if (err) {
    throw (err);
  }
  const film = JSON.parse(body);
  console.log(film.title);
});
