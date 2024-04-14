const fs = require('fs');

fs.readFile('file-data.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }

  console.log('File Content:');
  console.log(data);
});
module.exports = displayFileContent;