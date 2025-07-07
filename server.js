const express = require('express');
const cookieParser = require('cookie-parser');
const csrf = require('csurf');

const app = express();

app.use(cookieParser());

app.use(csrf({ cookie: true }));

app.use((req, res, next) => {
  res.cookie('XSRF-TOKEN', req.csrfToken());
  next();
});
const port = 3000; // You can change this if needed

app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.use((err, req, res, next) => {
  if (err.code === 'EBADCSRFTOKEN') {
    res.status(403).send('Invalid CSRF token');
  } else {
    next(err);
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
