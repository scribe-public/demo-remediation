const express = require('express');
const app = express();
const port = 3000; // You can change this if needed

app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
