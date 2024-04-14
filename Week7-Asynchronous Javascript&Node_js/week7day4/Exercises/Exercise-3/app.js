
const { readFile, writeFile } = require('./fileManager');


readFile('Hello World.txt')
  .then(content => {
    console.log('Content read from "Hello World.txt":', content);

    // Write content to "Bye World.txt"
    return writeFile('Bye World.txt', 'Writing to the file');
  })
  .then(successMessage => console.log(successMessage))
  .catch(error => console.error('Error:', error));
