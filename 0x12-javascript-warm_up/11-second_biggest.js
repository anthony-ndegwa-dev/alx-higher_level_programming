#!/usr/bin/node

let biggest = 0;
let i;
const numArray = [];

for (i = 2; i < process.argv.length; i++) {
  if (Number.isNaN(parseInt(process.argv[i])) === false) {
    numArray[i - 2] = parseInt(process.argv[i]);
  }
}

if (numArray.length > 1) {
  biggest = Math.max.apply(null, numArray);
  i = numArray.indexOf(biggest);
  numArray[i] = -Infinity;
  biggest = Math.max.apply(null, numArray);
}

console.log(biggest);
