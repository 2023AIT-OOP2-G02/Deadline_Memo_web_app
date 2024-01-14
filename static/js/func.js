//UUIDを生成して取得する関数
const getUUID = () => {
    return require('short-uuid').generate();
}

//日付を取得する関数
const unixtime = Date.now();
console.log(unixtime);

const nowDate = new Date(unixtime);

//24時間表記
const tokyoTimeStr = nowDate.toLocaleString('ja-JP', { timeZone: 'Asia/Tokyo' });
console.log(tokyoTimeStr);


//テストで関数実行
const newUUID = getUUID();
console.log(`新規UUID: ${newUUID}`); // ex: fDja8VuaVy4BGNfXDL1ghm


localStorage.setItem("sss", { "uajigejd": "jjj", "time": "jfiji"})