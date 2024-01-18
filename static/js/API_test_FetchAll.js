import { getUserID } from "./func.js";

const view_mydata = document.getElementById('view_mydata');

view_mydata.addEventListener('click', () => {
    const userID = getUserID();

    // FormDataオブジェクトを作成してJSON形式のデータをセット
	let fd = new FormData();
	fd.append("userID", userID);

    fetch("/API_test_FetchMyData", {method: "POST", body: fd}).then(response => {
        response.html().then(data => {
            window.location.href=data;
        });
    });
})