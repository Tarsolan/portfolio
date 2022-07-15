import React from "react";
import pushPin from "../../pictures/push_pin.png";
import styles from "./css/MissionBoard.module.css";

const MissionBoard = ({ missions }) => {
  return (
    <div id={styles.missionBoard}>
      <div id={styles.missionBoardHead}>
        <h2>Mission Board</h2>
      </div>
      {missions
        ? missions.map((mission) => {
            const {
              mission_num,
              job_name,
              job_description,
              payout,
              organization,
              deadline_date,
            } = mission;
            let date = new Date(deadline_date).toLocaleDateString();
            return (
              <div className={styles.missionInfo} key={mission_num}>
                <div className={styles.missionTop}>
                  <img
                    src={pushPin}
                    alt="A push pin to hold paper"
                    className={styles.missionPin}
                  />
                  <div className={styles.missionTitle}>{job_name}</div>
                  <div className={styles.missionClient}>{organization}</div>
                </div>

                <div className={styles.missionDesc}>{job_description}</div>

                <div className={styles.missionBottom}>
                  <div>Mission No: {mission_num}</div>
                  <div className={styles.missionDeadline}>
                    <span>Deadline:</span>
                    <span>{date}</span>
                  </div>
                  <div className={styles.missionPayout}>{payout}</div>
                </div>
              </div>
            );
          })
        : `There is no mission data available.`}
    </div>
  );
};

export default MissionBoard;
