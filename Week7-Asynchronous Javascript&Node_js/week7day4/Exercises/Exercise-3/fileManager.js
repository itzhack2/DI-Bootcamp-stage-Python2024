

const fs = require('fs');

// Function to read the content of a specified file
function readFile(fileName) {
  return new Promise((resolve, reject) => {
    fs.readFile(fileName, 'utf8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
}

// Function to write content to a specified file
function writeFile(fileName, content) {
  return new Promise((resolve, reject) => {
    fs.writeFile(fileName, content, 'utf8', (err) => {
      if (err) {
        reject(err);
      } else {
        resolve(`Content written to ${fileName}`);
      }
    });
  });
}

module.exports = { readFile, writeFile };
