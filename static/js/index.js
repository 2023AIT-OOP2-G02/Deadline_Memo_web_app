import { getUserID } from "./get_user_id.js";
import { update_remaining_time } from "./update_remaining_time.js";
import { update_tr_color } from "./update_tr_color.js";

// 日付の表示
const datetime = new Date().toLocaleString({ timeZone: 'Asia/Tokyo' }, { hour12: false });
const date = datetime.split(' ')[0];
const dateElement = document.getElementById('date');
dateElement.innerHTML = date;

// ユーザーIDを取得
const userID = getUserID();
console.log("ID:" + userID); //アクセスしてきた人のuserIDが表示されるはず

// deadline文字例を残り時間に変換する関数
// convert_remaining_time("2024-01-22 12:30:05");

// 全ての課題IDを取得

// 全てのtrタグを取得
const trs = document.getElementsByTagName('tr');

// HTMLCollectionを配列に変換
const trsArray = Array.from(trs);

// 先頭のtrタグを削除
trsArray.shift();

// trタグの配列をループ
trsArray.forEach(trElem => {
    // 課題IDを取得
    const kadaiID = trElem.id;
    console.log("kadaiID:" + kadaiID);

    // 課題をクリックしたら詳細ページへ移動
    trElem.addEventListener('click', () => {
        //
        location.href = `/detail_edit_page/${kadaiID}`;
    });
});


/* 期限を取得して残り時間に変換 */

// 全ての期限を取得
const deadlineElems = document.getElementsByClassName('deadline');

// HTMLCollectionを配列に変換
const deadlineElemArr = Array.from(deadlineElems);

//初回即時実行
update_remaining_time(deadlineElemArr); // 残り時間を更新
update_tr_color(deadlineElemArr); // 時間の背景色を変更

// 1秒おきにループさせる
setInterval(
    () => {
        update_remaining_time(deadlineElemArr);
        update_tr_color(deadlineElemArr);
    },
    1000
);




