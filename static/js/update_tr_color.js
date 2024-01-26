import { remaining_hour_minute } from "./remaining_hour_minute.js";

export const update_tr_color = (deadlineElemArr) => {
    deadlineElemArr.forEach(deadlineElem => {
        // elemのdata-deadlineを取得
        const deadline = deadlineElem.dataset.deadline;
        const temp = remaining_hour_minute(deadline);
        const day = temp[0];
        const hour = temp[1];
        const minute = temp[2];
        console.log(temp);



        if ((day === 0 && hour === 0 && minute === 0) || (day < 0 || hour < 0 || minute < 0)) {
            // どれかがマイナスの値&0の場合
            deadlineElem.style.background = "#e1e1e1";
        }
        else if (day < 1 && hour < 1 && minute < 60) {
            deadlineElem.style.background = "#ffa9a9";
        }
        else if (day < 1 && hour < 3) {
            deadlineElem.style.background = "#fdbea7";
        }
        else if (day < 1 && hour < 6) {
            deadlineElem.style.background = "#ffdab9";
        }
        else if (day < 1) {
            deadlineElem.style.background = "#fff7cc";
        }
        else if (day < 3) {
            deadlineElem.style.background = "#ffffe0";
        }
        else if (day < 7) {
            deadlineElem.style.background = "#fffdf0";
        }
    });
}