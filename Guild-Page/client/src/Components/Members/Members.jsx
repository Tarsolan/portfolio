import React from "react";
import { useNavigate } from "react-router-dom";
import usePagination from "../../Hooks/usePagination";
import styles from "./css/members.module.css";
import { AiOutlineArrowLeft, AiOutlineArrowRight } from "react-icons/ai";

const Main = ({ members, handleSelect }) => {
  const navigate = useNavigate();
  const goToMemberPage = (name) => navigate(`/members/info/${name}`);

  const onSelect = (member) => {
    handleSelect(member);
    goToMemberPage(member.full_name);
  };

  const paginate = usePagination(members, 6);
  console.log(`Current page: ${paginate.currentPage}`);
  return (
    <div id={styles.memberContainer}>
      <div id={styles.memberHead}>
        <span
          onClick={paginate.prev}
          className={
            paginate.currentPage === 1
              ? `${styles.arrow} ${styles.grey}`
              : styles.arrow
          }
        >
          <AiOutlineArrowLeft size={40} />
        </span>{" "}
        <h2>Member List</h2>
        <span
          onClick={paginate.next}
          className={
            paginate.currentPage === paginate.maxPage
              ? `${styles.arrow} ${styles.grey}`
              : styles.arrow
          }
        >
          <AiOutlineArrowRight size={40} />
        </span>
      </div>
      {members
        ? paginate.currentData().map((member) => {
            const { full_name, title, race, desc, rank_name, member_id } =
              member;
            return (
              <div
                className={styles.memberInfo + ` border${rank_name}`}
                onClick={() => onSelect(member)}
                key={member_id}
              >
                <div>
                  <div className={styles.memberName}>{full_name}</div>
                  {/* <div className="member-race">{member.race}</div> */}
                  <div className={styles.memberTitle}>
                    {title} - {race}
                  </div>
                </div>

                <div className={styles.memberDesc}>
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
