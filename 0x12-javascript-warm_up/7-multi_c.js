#!/usr/bin/node

const arg1 = process.argv[2];
const numberOfOccurrences = parseInt(arg1);

if (!isNaN(numberOfOccurrences)) {
  let i = 0;
  while (i < numberOfOccurrences) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
