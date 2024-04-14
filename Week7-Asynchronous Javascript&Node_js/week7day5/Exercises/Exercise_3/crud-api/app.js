const express = require('express');
const dataService = require ('./data/dataService.js');

const app = express()
const port = 5000;

app.get('/posts', async (req, res) => {
    try {
      const posts = await dataService.fetchPosts();
      res.json(posts);
      console.log('Data successfully retrieved and sent as a response.');
    } catch (error) {
      // Handle errors
      res.status(500).json({ error: 'Internal Server Error' });
      console.error('Error:', error.message);
    }
  });

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
