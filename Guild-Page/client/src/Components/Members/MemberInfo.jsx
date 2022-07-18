import React from "react";
import styles from "./css/memberInfo.module.css";

const MemberInfo = ({ member }) => {
  const {
    member_id,
    full_name,
    desc,
    title,
    join_date,
    rank_name,
    race,
    spec,
    image_url,
    completed,
  } = member;
  return (
    <div className={styles.singleMemberInfo}>
      <div className={styles.infoContainer}>
        <div>
          <img src={image_url} alt="Member" />
        </div>
        <div>
          <h2 className={styles.infoName}>{full_name}</h2>
          <p className={styles.infoTitle}>{title}</p>
          <div className={styles.memberRank + ` ${rank_name}`}>{rank_name}</div>
          <div className={styles.infoInfo}>
            <p>Member No: {member_id}</p>
            <p>Missions Completed: {completed ? completed : `0`}</p>
          </div>
          <div className={styles.infoSpecs}>
            <h3>Specialized Fields:</h3>
            <ul>
              {spec
                ? spec.map((speci) => <li key={speci}>{speci}</li>)
                : `No specs to show`}
            </ul>
          </div>
        </div>
      </div>
      <div className={styles.infoDesc}>
        <h2>Description</h2>
        <p>{desc ? desc : `No description available.`}</p>
      </div>
    </div>
  );
};

export default MemberInfo;
