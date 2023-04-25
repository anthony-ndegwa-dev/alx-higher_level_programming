#!/usr/bin/node
/**
 * A script that computes the number of tasks completed by user id
 * The first argument is the API URL:
 *  https://jsonplaceholder.typicode.com/todos
 * Only print users with completed task
 * You must use the module request
 */
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const resp = {};
    const json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      if (json[i].completed === true) {
        if (resp[json[i].userId] === undefined) {
          resp[json[i].userId] = 0;
        }
        resp[json[i].userId]++;
      }
    }
    console.log(resp);
  }
});
