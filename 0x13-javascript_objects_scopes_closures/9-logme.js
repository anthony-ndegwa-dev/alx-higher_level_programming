#!/usr/bin/node
let numarg = 0;

exports.logMe = function (item) {
  console.log(numarg + ': ' + item);
  numarg++;
};
