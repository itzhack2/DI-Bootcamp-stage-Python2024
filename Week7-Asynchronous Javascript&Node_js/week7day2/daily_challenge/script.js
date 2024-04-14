document.addEventListener('DOMContentLoaded', () => {
    const API_KEY = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My';
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const gifContainer = document.getElementById('gif-container');
    const deleteAllBtn = document.getElementById('delete-all-btn');
  
    searchForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const searchTerm = searchInput.value.trim();
      if (!searchTerm) return;
      
      try {
        const gifData = await fetchRandomGif(searchTerm);
        const gifUrl = gifData.images.fixed_height.url;
        appendGif(gifUrl, searchTerm);
      } catch (error) {
        console.error('Error fetching random gif:', error);
      }
    });
    deleteAllBtn.addEventListener('click', () => {
      gifContainer.innerHTML = '';
    });
    function fetchRandomGif(category) {
      const apiUrl = `https://api.giphy.com/v1/gifs/random?tag=${category}&api_key=${API_KEY}`;
      return fetch(apiUrl)
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        });
    }
    function appendGif(gifUrl, category) {
      const gifElement = document.createElement('div');
      gifElement.innerHTML = `
        <img src="${gifUrl}" alt="${category} gif">
        <button class="delete-btn">Delete</button>
      `;
      gifContainer.appendChild(gifElement);
  
      const deleteBtn = gifElement.querySelector('.delete-btn');
      deleteBtn.addEventListener('click', () => {
        gifContainer.removeChild(gifElement);
      });
    }
  });
  