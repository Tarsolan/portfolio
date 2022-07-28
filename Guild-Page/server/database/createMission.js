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

const editMission = async (body) => {
  const { mission_num, newName, newDesc, newPay, newDate } = body;
  let sql = `UPDATE part2.mission
	SET job_name='${newName}', job_description='${newDesc}', payout='${newPay}', deadline_date='${newDate}'
	WHERE mission_num=${mission_num};`;

  let res = await db.query(sql);

  return res.rows;
};

module.exports = { addMission, editMission };
