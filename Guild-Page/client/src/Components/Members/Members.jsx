import React from "react";
import { useNavigate } from "react-router-dom";
import styles from "./css/members.module.css";

const Main = ({ members, handleSelect }) => {
  const navigate = useNavigate();
  const goToMemberPage = (name) => navigate(`/members/info/${name}`);

  const onSelect = (member) => {
    handleSelect(member);
    goToMemberPage(member.full_name);
  };

  return (
    <div id={styles.memberContainer}>
      <h2 id={styles.memberHead}>Member List</h2>
      {members
        ? members.map((member) => {
            const { full_name, title, race, desc, rank_name, member_id } =
              member;
            return (
              <div
                className={styles.memberInfo + ` border${rank_name}`}
                onClick={() => onSelect(member)}
                key={member_id}
              >
                {/* <img src="" alt="Member photo" /> */}
                <div>
                  <div className={styles.memberName}>{full_name}</div>
                  {/* <div className="member-race">{member.race}</div> */}
                  <div className={styles.memberTitle}>
                    {title} - {race}
                  </div>
                </div>

                <div className={styles.memberDesc}>
                  {/* {member.desc} */}
                  {desc === null ? `No description available.` : desc}
                </div>
                <div className={styles.memberId}>Member No: {member_id}</div>
                {/* <div>
                  <div className={`member-rank ${rank_name}`}>{rank_name}</div>
                  <div className="member-id">Member No: {member_id}</div>
                </div> */}
              </div>
            );
          })
        : `There is no member data available.`}
    </div>
  );
};

export default Main;
