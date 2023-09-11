#!/usr/bin/node

const arg1 = process.argv[2];
const parsedInt = parseInt(arg1, 10);

if (!isNaN(parsedInt) && Number.isInteger(parsedInt)) {
  console.log(`My number: ${parsedInt}`);
} else {
  console.log('Not a number');
}
