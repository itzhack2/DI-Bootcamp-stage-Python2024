// Exercise 1: Fetch API
fetch("https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My")
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error('There was a problem with the fetch operation:', error));

// Exercise 2: Giphy API
fetch("https://api.giphy.com/v1/gifs/search?q=sun&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&limit=10&offset=2")
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error('There was a problem with the fetch operation:', error));

// Exercise 3: Async Function
async function fetchStarWars() {
  try {
    const response = await fetch("https://www.swapi.tech/api/starships/9/");
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const objectStarWars = await response.json();
    console.log(objectStarWars.result);
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  }
}
fetchStarWars();

// Exercise 4: Analyze
function resolveAfter2Seconds() {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve('resolved');
    }, 2000);
  });
}

async function asyncCall() {
  console.log('calling');
  let result = await resolveAfter2Seconds();
  console.log(result);
}
asyncCall();
// the final outcome will be:calling resolved
// 