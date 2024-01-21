
export const convert_remaining_time = () => {
    // 最終的に受け取る引数: 2024-01-21 21:03:00

    // 仮データ、本番はDBから取得
    const year_deadline = 2024;
    const month_deadline = 2;
    const day_deadline = 21;
    const hour_deadline = 18;
    const minute_deadline = 30;
    const second_deadline = 0;

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

    console.log("秒数の差: " + diff_sec + "秒");

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

    if (diff_sec > year_sec) {
        // ex:年単位の場合

        // 1つの文字例に変換
        result_time_str = `${diff_year}年`;
        if (diff_month !== 0) { // 0ヶ月の場合は表示しない
            result_time_str += ` ${diff_month}ヶ月`;
        }
    }
    else if (diff_sec > month_sec) {
        // 月単位の場合

        // 1つの文字例に変換
        result_time_str = `${diff_month}ヶ月`;
        if (diff_day !== 0) { // 0日の場合は表示しない
            result_time_str += ` ${diff_month}日`;
        }
    }
    else if (diff_sec > day_sec) {
        // 日単位の場合

        result_time_str = `${diff_day}日`;
        if (diff_hour !== 0) { // 0時間の場合は表示しない
            result_time_str += ` ${diff_hour}時間`;
        }
    }
    else if (diff_sec > hour_sec) {
        // 時間単位の場合

        result_time_str = `${diff_hour}時間`;
        if (diff_minute !== 0) { // 0分の場合は表示しない
            result_time_str += ` ${diff_minute}分`;
        }
    }
    else if (diff_sec > minute_sec) {
        // 分単位の場合

        result_time_str = `${diff_minute}分`;
        if (diff_second !== 0) { // 0秒の場合は表示しない
            result_time_str += ` ${diff_second}秒`;
        }
    }
    else if (diff_sec > 0) {
        // 秒単位の場合

        result_time_str = `${diff_sec}秒`;
    }
    else if (diff_sec == 0 || diff_sec < 0) {
        // 時間切れの場合
        result_time_str = `0秒`;
    }

    // 上記の年単位と同様に、月、日、時間、分、秒の単位に変換する
    // 基本的に、大きい単位と1つ小さい単位の組み合わせで表示する
    // ex: 2年 1ヶ月
    //     1ヶ月 2日
    //     2日 3時間
    //     3時間 4分
    //     4分 5秒
    //     5秒
    //     0秒
    // 時間切れの場合(diff_secが0だったり)は0秒になるようにする


    // デバック用
    console.log("残り時間：" + result_time_str);
}