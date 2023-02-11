#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) console.log(err);
  const films = JSON.parse(body).results.filter(
    function (film) {
      return film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
    }
  );
  console.log(films.length);
});
