#!/usr/bin/node

const fs = require('fs');
const targetFileName = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(targetFileName, contentToWrite, 'utf-8', (writeError) => {
    if (writeError) {
        console.log(writeError);
    }
});