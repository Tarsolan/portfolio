import React from "react";
import { AiOutlineArrowLeft, AiOutlineArrowRight } from "react-icons/ai";
import styles from "./css/MembersInfo.module.css";

const Arrow = ({ side, paginate }) => {
	return (
		<>
			{side === "left" ? (
				<span
					onClick={paginate.prev}
					className={
						paginate.currentPage === 1
							? `${styles.leftArrow} ${styles.grey}`
							: styles.leftArrow
					}
				>
					<AiOutlineArrowLeft size={40} />
				</span>
			) : (
				<span
					onClick={paginate.next}
					className={
						paginate.currentPage === paginate.maxPage
							? `${styles.rightArrow} ${styles.grey}`
							: styles.rightArrow
					}
				>
					<AiOutlineArrowRight size={40} />
				</span>
			)}
		</>
	);
};

export default Arrow;
