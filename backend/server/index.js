// eslint-disable-next-line strict
const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const cookieParser = require("cookie-parser");
const app = express();
app.use(cookieParser());

const session = require("express-session");

app.use(session({
    secret: "secret",
    resave: false,
    httpOnly: true,
    saveUninitialized: true,
    cookie: {
        secure: false,
        maxAge: 60000
    }
}));

app.use(bodyParser.json());
app.use(cors({
    "origin": ["http://localhost:8080"],
    "credentials": true,
    "methods": ["GET", "POST"]
}));
const port = process.env.PORT || 5000;

app.listen(port, () => console.log(`server started on ${port}`));
