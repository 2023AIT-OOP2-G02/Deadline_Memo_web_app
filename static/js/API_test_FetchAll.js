import { getUserID } from "./func.js";

const view_mydata = document.getElementById('view_mydata');
const userID = getUserID();

// FormDataオブジェクトを作成してJSON形式のデータをセット
let fd = new FormData();
fd.append("userID", userID);

view_mydata.addEventListener('click', () => {
    fetch("/API_test_FetchMyData", { method: "POST", body: fd }).then(response => {
        response.json().then(data => {
            window.location.href=data.redirect;
        });
    });
})

const div_view_jsonData = document.getElementById('view_jsonData');
fetch("/fetch_all_data", { method: "POST", body: fd }).then(response => {
    response.json().then(data => {
        div_view_jsonData.innerHTML = data;
    });
});