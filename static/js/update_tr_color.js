import { remaining_hour_minute } from "./remaining_hour_minute.js";

export const update_tr_color = (deadlineElemArr) => {
    deadlineElemArr.forEach(deadlineElem => {
        // elemのdata-deadlineを取得
        const deadline = deadlineElem.dataset.deadline;
        const temp = remaining_hour_minute(deadline);
        const hour = temp[0];
        const minute = temp[1];

        if (hour < 1 && minute < 10) {
            // 赤色にする (10分以下)
            deadlineElem.style.background = "red";
        } else if (hour < 1 && minute < 30) {
            // ピンク色にする (30分以下)
            deadlineElem.style.background = "pink";
        } else if (hour < 1 && minute < 60) {
            // 黄色にする (1時間以下)
            deadlineElem.style.background = "yellow";
        } else if (hour < 6) {
            // 緑色にする (6時間以下)
            deadlineElem.style.background = "green";
        }
    });
}