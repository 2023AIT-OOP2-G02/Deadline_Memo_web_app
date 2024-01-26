export const remaining_hour_minute = (deadline_data) => {
    // 最終的に受け取る引数: 2024-01-21 21:03:00

    // 引数から -, :, 半角スペースを除く
    const deadline_splitdata = deadline_data.split(/[-:\s]/);
    // 仮データ、本番はDBから取得
    const year_deadline = Number(deadline_splitdata[0]);
    const month_deadline = Number(deadline_splitdata[1]);
    const day_deadline = Number(deadline_splitdata[2]);
    const hour_deadline = Number(deadline_splitdata[3]);
    const minute_deadline = Number(deadline_splitdata[4]);
    const second_deadline = Number(deadline_splitdata[5]);

    let today = new Date();

    // 現在時刻から年月日時分秒を取得
    let year_now = today.getFullYear();
    let month_now = today.getMonth() + 1;
    let day_now = today.getDate();
    let hour_now = today.getHours();
    let minute_now = today.getMinutes();
    let second_now = today.getSeconds();

    // deadlineをDate型に変換
    const date_deadline = new Date(
        year_deadline,
        month_deadline - 1,
        day_deadline,
        hour_deadline,
        minute_deadline,
        second_deadline
    );

    // 現在時刻をDate型に変換
    const date_now = new Date(
        year_now,
        month_now - 1,
        day_now,
        hour_now,
        minute_now,
        second_now
    );

    // 差分の秒数を計算
    const diff_sec = (date_deadline.getTime() - date_now.getTime()) / 1000;

    // console.log("秒数の差: " + diff_sec + "秒");

    // 秒数を適切な単位に変換
    let result_time_str = "";
    // 単位ごとの秒数を定数化しておくと便利
    const year_sec = 31536000; // 1年の秒数
    const month_sec = 2592000; // 1ヶ月(30日)の秒数
    const day_sec = 86400; // 1日の秒数
    const hour_sec = 3600; // 1時間の秒数
    const minute_sec = 60; // 1分の秒数
    const second_sec = 1; // 1秒の秒数
    const diff_year = Math.floor(diff_sec / year_sec);
    const diff_month = Math.floor((diff_sec - diff_year * year_sec) / month_sec);
    const diff_day = Math.floor((diff_sec - diff_month * month_sec) / day_sec);
    const diff_hour = Math.floor((diff_sec - diff_day * day_sec) / hour_sec);
    const diff_minute = Math.floor((diff_sec - diff_hour * hour_sec) / minute_sec);
    const diff_second = Math.floor((diff_sec - diff_minute * minute_sec) / second_sec);

    return [diff_day, diff_hour, diff_minute];
}