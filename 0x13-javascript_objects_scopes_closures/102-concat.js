#!/usr/bin/node
const fs = require('fs');
const [sourceFile1, sourceFile2, destinationFile] = process.argv.slice(2);

const content1 = fs.readFileSync(sourceFile1, 'utf8');

const content2 = fs.readFileSync(sourceFile2, 'utf8');

const concatenatedContent = content1 + '\n' + content2 + '\n';

fs.writeFileSync(destinationFile, concatenatedContent);

console.log(`Concatenated ${sourceFile1} and ${sourceFile2} to ${destinationFile}`);
