import { getUserID } from "./func.js";

const post_button = document.getElementById('post');
const input_kadai_id = document.getElementById('kadai_id');

post_button.addEventListener('click', () => {

    let kadai_id = input_kadai_id.value;

    // fetch api で POST

    // FormDataオブジェクトを作成してJSON形式のデータをセット
    let fd = new FormData();
    fd.append("kadai_id", kadai_id);

    // 送信先 : /remove_data
    fetch("/remove_data", { method: "POST", body: fd }).then(response => {
        //fetch("/remove_data?" + kadai_id.toString()).then(response => {
        response.json().then(data => {
            console.log(data);
        });
    });

});