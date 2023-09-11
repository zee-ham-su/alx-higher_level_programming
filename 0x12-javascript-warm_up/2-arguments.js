#!/usr/bin/node

const argCount = process.argv.length - 2;
const message = argCount > 0 ? (argCount === 1 ? 'Argument found' : 'Arguments found') : 'No argument';
console.log(message);
