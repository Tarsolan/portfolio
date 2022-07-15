const { Pool } = require("pg");

let pool = new Pool({
  host: "localhost",
  user: "alex",
  port: 5432,
  password: "password",
  database: "The_Guild",
});

module.exports = pool;
