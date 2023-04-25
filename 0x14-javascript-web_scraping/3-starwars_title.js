#!/usr/bin/node
// script that displays the title of the Star Wars movie using API

const request = require('request');
let url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
