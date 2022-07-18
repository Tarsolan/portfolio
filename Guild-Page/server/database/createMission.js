const db = require("./pgAdmin");

const addMission = async (body) => {
  const {
    missionTitle,
    missionDesc,
    missionPayout,
    missionDeadline,
    client_id,
  } = body;
  let newMission = `INSERT INTO part2.mission(
      job_name, job_description, payout, deadline_date, client_id)
      VALUES ('${missionTitle}', '${missionDesc}', '${missionPayout}', '${missionDeadline}', '${client_id}');`;

  let res = await db.query(newMission);

  return res.rows;
};

module.exports = { addMission };
