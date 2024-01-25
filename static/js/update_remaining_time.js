import { convert_remaining_time } from "./convert_remaining_time.js";

export const update_remaining_time = (deadlineElemArr) => {
    deadlineElemArr.forEach(deadlineElem => {
        // elemのdata-deadlineを取得
        const deadline = deadlineElem.dataset.deadline;

        // deadlineを残り時間に変換
        const remaining_time = convert_remaining_time(deadline);
        
        // 残り時間を表示
        deadlineElem.innerHTML = remaining_time;

        

    });
}