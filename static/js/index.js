import { getUserID } from "./get_user_id.js";
import { convert_remaining_time } from "./convert_remaining_time.js";

const datetime = new Date().toLocaleString({ timeZone: 'Asia/Tokyo' }, { hour12: false });
const date = datetime.split(' ')[0];

const dateElement = document.getElementById('date');
dateElement.innerHTML = date;


const userID = getUserID();
console.log("ID:" + userID); //アクセスしてきた人のuserIDが表示されるはず

convert_remaining_time();
