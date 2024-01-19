import { getUserID } from "./get_user_id.js";

//userIDを取得
const userID = getUserID();

//formにuserIDを埋め込む
const inputElem = document.getElementById("required-userID");
inputElem.value = `${userID}`;
// inputElem.innerHTML = userID;

console.log(inputElem.value)

