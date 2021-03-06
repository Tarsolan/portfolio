import React from "react";
import styles from "./css/ClientDisplay.module.css";
import { useNavigate } from "react-router-dom";
import { useState } from "react";

const ClientDisplay = ({ client, missionInfo, handleSelect }) => {
	const {
		client_id,
		status,
		description,
		contact_name,
		organization,
		missions,
	} = client;

	const [showDetail, setShowDetails] = useState(false);
	// let date = new Date(join_date).toLocaleDateString();

	const navigate = useNavigate();
	const goToEditDetails = () => navigate("/account/client/info/edit");
	const goToMissionPage = (num) => navigate(`/missions/info/${num}`);

	const missionSelect = (num) => {
		handleSelect(num);
		goToMissionPage(num);
	};

	const missionNames = (missionInfo) => {
		var missionArr = [];
		missionInfo.forEach((mission) => {
			missions.forEach((mission_id) => {
				if (mission_id === mission.mission_num) {
					missionArr.push(mission);
				}
			});
		});
		var missionNames = missionArr.map((mission) => {
			return (
				<div
					onClick={() => missionSelect(mission.mission_num)}
					className={styles.displayMission}
				>
					<span key={mission.mission_num}>
						<h4>
							{mission.mission_num} - {mission.job_name}
						</h4>
						<p>{mission.job_description}</p>
					</span>
				</div>
			);
		});
		return missionNames;
	};

	return (
		<div className={styles.memberDisplay}>
			<h2>Account Details</h2>
			<div className={styles.container}>
				<div className={styles.leftSide}>
					<div className={styles.displayRow}>
						<label>Contact Name:</label>
						<div>{contact_name}</div>
					</div>
					<div className={styles.displayRow}>
						<label>Organization:</label>
						<div>{organization}</div>
					</div>
				</div>
				<div>
					<div className={styles.displayRow}>
						<label>Client ID:</label>
						<div>{client_id}</div>
					</div>
					<div className={styles.displayRow}>
						<label>Status:</label>
						<div>{status ? `Active` : `Inactive`}</div>
					</div>
				</div>
			</div>
			<hr />
			<div className={styles.displayRowDesc}>
				<label>Description:</label>
				<div>{description}</div>
			</div>
			<hr />

			{showDetail ? (
				<div className={styles.displayRowBottom}>
					{/* We would like this section to contain links to the relevant mission reports */}
					<h3>
						<label>Mission Details:</label>
					</h3>
					<div>
						{missions ? (
							<div className={styles.missionList}>
								{missionNames(missionInfo)}
							</div>
						) : (
							`No jobs to show.`
						)}
					</div>
				</div>
			) : (
				<></>
			)}

			<div className={styles.displayButton}>
				<button
					onClick={() => setShowDetails(!showDetail)}
					className={styles.detailButton}
				>
					{showDetail ? `Hide Mission Details` : `Expand Mission Details`}
				</button>
				<div>
					<button className="btn btn-primary" onClick={goToEditDetails}>
						Edit Account Details
					</button>
					<div>
						<a href="http://localhost:3000/">Change Password</a>
					</div>
				</div>
			</div>
		</div>
	);
};

export default ClientDisplay;
