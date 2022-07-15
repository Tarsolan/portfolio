const express = require("express");
const router = express.Router();

const { addMission } = require("../database/createMission");
const { getMissions } = require("../database/fetchDataList");

router.get("/", (req, res) => {
  DEBUG && console.log(req.url);
  getMissions()
    .then((response) => {
      res.status(200).send(response);
    })
    .catch((error) => {
      res.status(500).send(error);
    });
});

router.post("/new", async (req, res) => {
  let response = await addMission(req.body);
  res.status(200).send(response);
});

module.exports = router;
