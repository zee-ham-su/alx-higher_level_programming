#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const completedTasksCount = {};
    const tasks = JSON.parse(body);

    for (const taskIndex in tasks) {
      const currentTask = tasks[taskIndex];

      if (currentTask.completed === true) {
        if (completedTasksCount[currentTask.userId] === undefined) {
          completedTasksCount[currentTask.userId] = 1;
        } else {
          completedTasksCount[currentTask.userId]++;
        }
      }
    }

    console.log(completedTasksCount);
  } else {
    console.error('An error occurred. Status code: ' + response.statusCode);
  }
});
