
const chalk = require('chalk');

function displayColorfulMessage() {
  const colorfulMessage = chalk.bold.blue('Hello, ') + chalk.bold.green('Node.js Enthusiast') + chalk.bold.red('!');
  console.log(colorfulMessage);
}

module.exports = displayColorfulMessage();
