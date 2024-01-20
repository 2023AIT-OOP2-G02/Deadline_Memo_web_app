
export const convert_remaining_time = () => {
    // 最終的に受け取る引数: 2024-01-21 21:03:00

    // 仮データ、本番はDBから取得
    const year_deadline = 2026;
    const month_deadline = 2;
    const day_deadline = 21;
    const hour_deadline = 21;
    const minute_deadline = 40;
    const second_deadline = 0;

    // 仮データ、本番はnew Date()で現在時刻を取得
    const year_now = 2024;
    const month_now = 1;
    const day_now = 21;
    const hour_now = 21;
    const minute_now = 30;
    const second_now = 0;

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

    if (diff_sec > year_sec) {
        // ex:年単位の場合
        const diff_year = Math.floor(diff_sec / year_sec);
        const diff_month = Math.floor((diff_sec - diff_year * year_sec) / month_sec);
        // 1つの文字例に変換
        result_time_str = `${diff_year}年`;
        if (diff_month !== 0) { // 0ヶ月の場合は表示しない
            result_time_str += ` ${diff_month}ヶ月`;
        }
    }
    // TODO: ここから下のelse if()を実装する
    // else if ()・・・
    // else if ()・・・

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