const db = require("./pgAdmin");

const editMember = async (body) => {
  const {
    member_id,
    firstName,
    lastName,
    raceID,
    newTitle,
    filterDescription,
    rankID,
  } = body;
  let editMem = `UPDATE part2.member
	SET first_name='${firstName}', last_name='${lastName}', title='${newTitle}', rank_id=${rankID}, race_id=${raceID}, description='${filterDescription}'
	WHERE member_id=${member_id};`;

  try {
    let res = await db.query(editMem);

    return res.rows;
  } catch (error) {
    console.log(error);
  }
};

const editMemberSpec = async (specArr, member_id) => {
  let deleteSpec = `DELETE FROM part2.member_spec
  WHERE member_id=${member_id};`;

  let res = await db.query(deleteSpec);

  specArr.map(async (spec) => {
    let editMemSpec = `INSERT INTO part2.member_spec(
         spec_id, member_id)
         VALUES (${spec}, ${member_id});`;

    let res = await db.query(editMemSpec);
    return res.rows;
  });

  return res.rows;
};

const editMemberPoints = async (body, member_id) => {
  const { point_total } = body;
  let sql = `UPDATE part2.member
	SET point_total=$1
	WHERE member_id=$2`;

  try {
    let res = await db.query(sql, [point_total, member_id]);
    return res.rows;
  } catch (error) {
    console.log(error);
  }
};

// const addMemberSpecs = async (body) => {
//     const { specArr, nextID } = body;
//     specArr.map(async (spec) => {
//       let specQuery = `INSERT INTO part2.member_spec(
//         spec_id, member_id)
//         VALUES (${spec}, ${nextID});`;

//       let res = await db.query(specQuery);
//       return res.rows;
//     });
//   };

module.exports = { editMember, editMemberSpec, editMemberPoints };
