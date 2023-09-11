#!/usr/bin/node

const args = process.argv.slice(2);
const numbers = args.map(arg => parseInt(arg)).filter(num => !isNaN(num));

const max = Math.max.apply(null, numbers);
const secondLargest = Math.max.apply(null, numbers.filter(num => num < max));

console.log(args.length <= 1 ? 0 : secondLargest || 0);
