import { getUserID } from "./get_user_id.js";

// userIDを取得する
const userID = getUserID();

// FormDataオブジェクトを作成してJSON形式のデータをセット
let fd = new FormData();
fd.append("userID", userID);
fetch("/fetch_remove_data", { method: "POST", body: fd }).then(response => {
    response.json().then(data => {
        // jsからリンク変更
        window.location.href = data.redirect;
    });
});
