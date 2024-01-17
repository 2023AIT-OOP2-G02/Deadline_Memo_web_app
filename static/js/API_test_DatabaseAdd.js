import { getUserID } from "./func.js";

const input_title = document.getElementById('title');
const input_subject = document.getElementById('subject');
const input_deadline_date = document.getElementById('deadline_date');
const input_deadline_time = document.getElementById('deadline_time');
const input_memo = document.getElementById('memo');

const post_button = document.getElementById('post');

post_button.addEventListener('click', () => {
    let title = input_title.value;
    let subject = input_subject.value;
    let deadline_date = input_deadline_date.value;
    let deadline_time = input_deadline_time.value;
    let memo = input_memo.value;

    let deadline = deadline_date.toString() + " " + deadline_time.toString();

    let uuid = self.crypto.randomUUID(); // 課題id
    // console.log(uuid);

    const userID = getUserID();

    let datetime = new Date().toLocaleString({ timeZone: 'Asia/Tokyo' }, { hour12: false });
    // console.log(datetime);

    let data = {
        uuid: {
            "title": title,
            "subject": subject,
            "deadline": deadline,
            "memo": memo,
            "memo_img": "nothing",
            "created_at": datetime,
            "updated_at": datetime,
            "created_by": userID,
        }
    };

    // fetch api で POST

    // 送信先 : /add_data
    fetch("/add_data", {method: "POST", body: data}).then(response => {
        response.json().then(data => {
            console.log(data);
        });
    });

});