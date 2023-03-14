#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nbOccurrences = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      nbOccurrences++;
    }
  }
  return nbOccurrences;
};
