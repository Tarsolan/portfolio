const express = require("express");
const app = express();
const port = 3001;
global.DEBUG = true;

app.use(express.json());
app.use(function (req, res, next) {
  res.setHeader("Access-Control-Allow-Origin", "http://localhost:3000");
  res.setHeader("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,OPTIONS");
  res.setHeader(
    "Access-Control-Allow-Headers",
    "Content-Type, Access-Control-Allow-Headers"
  );
  next();
});

const newMemberRouter = require("./routes/register");
const missionRouter = require("./routes/missions");
const memberRouter = require("./routes/members");
const raceRouter = require("./routes/races");
const clientRouter = require("./routes/clients");
const specRouter = require("./routes/specs");

app.use("/register", newMemberRouter);
app.use("/members", memberRouter);
app.use("/races", raceRouter);
app.use("/missions", missionRouter);
app.use("/clients", clientRouter);
app.use("/specs", specRouter);

// TO DO
// View Mission

app.listen(port, () => {
  console.log(`App running on port ${port}.`);
});
