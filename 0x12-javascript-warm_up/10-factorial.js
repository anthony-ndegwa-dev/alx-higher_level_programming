#!/usr/bin/node
function factorial (num) {
  if ((Number.isNaN(num)) || (num === 1)) {
    return 1;
  }
  return factorial(num - 1) * num;
}
console.log(factorial(parseInt(process.argv[2])));
