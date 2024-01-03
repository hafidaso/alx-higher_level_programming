#!/usr/bin/node

const request = require('request');
const characterId = '18';
let characterUrl = 'https://swapi-api.alx-tools.com/api/people/';
characterUrl += characterId + '/';
const requestUrl = process.argv[2];

request(requestUrl, (err, response, body) => {
  if (err) {
    throw (err);
  }
  const film = JSON.parse(body);
  let noEpisodes = 0;
  const results = film.results;
  for (const result of results) {
    const characters = result.characters;
    const wedgeCharacter = characters.filter(n => n === characterUrl);
    noEpisodes += wedgeCharacter.length;
  }
  console.log(noEpisodes);
});
