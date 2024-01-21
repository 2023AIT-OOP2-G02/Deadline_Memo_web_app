import { getUserID } from "./get_user_id.js";

// 日付の表示
const datetime = new Date().toLocaleString({ timeZone: 'Asia/Tokyo' }, { hour12: false });
const date = datetime.split(' ')[0];
const dateElement = document.getElementById('date');
dateElement.innerHTML = date;

// ユーザーIDを取得
const userID = getUserID();
console.log("ID:" + userID); //アクセスしてきた人のuserIDが表示されるはず

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