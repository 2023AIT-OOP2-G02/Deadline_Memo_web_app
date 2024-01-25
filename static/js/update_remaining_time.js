import { convert_remaining_time } from "./convert_remaining_time.js";
import { sendPushNotification } from "./push_notice.js"

export const update_remaining_time = (deadlineElemArr) => {
    deadlineElemArr.forEach(deadlineElem => {
        // elemのdata-deadlineを取得
        const deadline = deadlineElem.dataset.deadline;
        const title = deadlineElem.dataset.title;

        // deadlineを残り時間に変換
        deadlineElem.innerHTML = convert_remaining_time(deadline);
        sendPushNotification(title, deadlineElem.innerHTML);
    });
}