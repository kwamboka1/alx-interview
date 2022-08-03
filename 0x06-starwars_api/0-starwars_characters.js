#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const baseUrl = 'https://swapi-api.hbtn.io/api/';

request.get(`${baseUrl}films/${movieId}`, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  const result = body.characters;
  // console.log(result);

  actorsList(result);
});

function actorsList (result, i = 0) {
  if (i === result.length) return;

  request(result[i], { json: true }, (err, res, body) => {
    if (err) { return console.log(err); }

    console.log(body.name);
    actorsList(result, i + 1);
  });
}
