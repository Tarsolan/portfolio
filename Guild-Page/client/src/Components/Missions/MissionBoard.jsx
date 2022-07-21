import React from "react";
import { useNavigate } from "react-router-dom";
import usePagination from "../../Hooks/usePagination";
import pushPin from "../../pictures/push_pin.png";
import styles from "./css/MissionBoard.module.css";

const MissionBoard = ({ missions, handleSelect }) => {
  const paginate = usePagination(missions, 3);
  const navigate = useNavigate();
  const goToMissionPage = (num) => navigate(`/missions/info/${num}`);

  const onSelect = (mission) => {
    handleSelect(mission);
    goToMissionPage(mission.mission_num);
  };

  return (
    <>
      {missions && (
        <div id={styles.missionBoardHead}>
          {[...Array(paginate.maxPage)].map((e, page) => {
            return (
              <button
                key={page}
                onClick={(e) => paginate.jump(e.target.value)}
                value={page}
              >
                {page}
              </button>
            );
          })}
        </div>
      )}
      <div id={styles.missionBoard}>
        {missions
          ? paginate.currentData().map((mission) => {
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
                <div
                  className={styles.missionInfo}
                  key={mission_num}
                  onClick={() => onSelect(mission)}
                >
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
    </>
  );
};

export default MissionBoard;
