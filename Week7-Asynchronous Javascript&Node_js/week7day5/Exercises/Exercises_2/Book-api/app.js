
const express = require('express');
const app = express();
const port = 3000;

// Define a basic data array containing a few book objects. Each book object should have properties like id, title, author, and publishedYear.
const books = [
  { id: 1, title: 'The Great Gatsby', author: 'F. Scott Fitzgerald', publishedYear: 2020 },
  { id: 2, title: 'To Kill a Mockingbird', author:  'Harper Lee', publishedYear: 2021 },
  
];

// Middleware to parse JSON body content
app.use(express.json());

// Read all books route
app.get('/api/books', (req, res) => {
  res.json(books);
});

// Read a specific book route
app.get('/api/books/:bookId', (req, res) => {
  const bookId = parseInt(req.params.bookId);
  const book = books.find(book => book.id === bookId);
  if (book) {
    res.json(book);
  } else {
    res.status(404).send('Book not found');
  }
});

// Create a new book route
app.post('/api/books', (req, res) => {
  const { title, author, publishedYear } = req.body;
  const newBook = {
    id: books.length + 1,
    title,
    author,
    publishedYear,
  };

  books.push(newBook);
  res.status(201).json(newBook);
});

// Server listening on port 5000
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
