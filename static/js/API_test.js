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

    let uuid = self.crypto.randomUUID();
    console.log(uuid);

    let data = {
        "title": title,
        "subject": subject,
        "deadline_date": deadline_date,
        "deadline_time": deadline_time,
        "memo": memo
    };
});