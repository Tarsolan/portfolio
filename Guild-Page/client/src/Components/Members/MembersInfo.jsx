import React, { useEffect } from "react";
import usePagination from "../../Hooks/usePagination";
import MemberInfo from "./MemberInfo";
import styles from "./css/MembersInfo.module.css";
import Arrow from "./Arrow";

const MembersInfo = ({ members, selectedMember }) => {
	const paginate = usePagination(members, 1);
	console.log(paginate);

	useEffect(() => {
		const findMember = () => {
			let id_count = 1;

			var pageNum = members.map((member) => {
				console.log(`Current ID: ${member.member_id}`);
				console.log(`Target Id: ${selectedMember.member_id}`);
				console.log(`Current Page Number: ${id_count}`);
				if (member.member_id !== selectedMember.member_id) {
					id_count++;
				} else {
					console.log("Match found!");
					paginate.jump(id_count);
					return id_count;
				}
			});

			//paginate.jump(pageNum);
		};

		findMember();
	}, []);

	return (
		<div className={styles.singleMember}>
			<Arrow side={"left"} paginate={paginate} />
			{paginate.currentData().map((member) => {
				return <MemberInfo member={member} />;
			})}
			<Arrow side={"right"} paginate={paginate} />
		</div>
	);
};

export default MembersInfo;
