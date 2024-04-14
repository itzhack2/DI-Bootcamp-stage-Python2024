const express = require('express');
const app = express();
const port = 3000;

const posts = [
  { id: 1, title: 'First Post', content: 'This is the content of the first post.' },
  { id: 2, title: 'Second Post', content: 'This is the content of the second post.' },

];

app.use(express.json());

app.get('/posts', (req, res) => {
  res.json(posts);
});

app.get('/posts/:id', (req, res) => {
  const postId = parseInt(req.params.id);
  const post = posts.find(post => post.id === postId);

  if (post) {
    res.json(post);
  } else {
    res.status(404).send('Post not found');
  }
});

// Create a new blog post
app.post('/posts', (req, res) => {
  const { title, content } = req.body;
  const newPost = {
    id: posts.length + 1,
    title,
    content,
  };

  posts.push(newPost);
  res.status(201).json(newPost);
});


app.put('/posts/:id', (req, res) => {
  const postId = parseInt(req.params.id);
  const postIndex = posts.findIndex(post => post.id === postId);

  if (postIndex !== -1) {
    const updatedPost = {
      id: postId,
      title: req.body.title || posts[postIndex].title,
      content: req.body.content || posts[postIndex].content,
    };

    posts[postIndex] = updatedPost;
    res.json(updatedPost);
  } else {
    res.status(404).send('Post not found');
  }
});


app.delete('/posts/:id', (req, res) => {
  const postId = parseInt(req.params.id);
  const postIndex = posts.findIndex(post => post.id === postId);

  if (postIndex !== -1) {
    posts.splice(postIndex, 1);
    res.send('Post deleted successfully');
  } else {
    res.status(404).send('Post not found');
  }
});


app.use((req, res) => {
  res.status(404).send('Invalid route');
});


app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Server error');
});


app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
// const express = require ("express")
// const app = express()
// const port = 3000

// app.get("/" , (req,res)=>{
//     res.send("hello world!")
// })

// app.listen(port,()=>{
//     console.log(`app listening on port ${port}`);
// })
// server.js