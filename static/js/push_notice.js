/**
 * MacOSの場合、左上のシステム設定から集中モード、おやすみモードをoffにする。
 * 通知の設定から使用するブラウザの通知をonにしておく
 * Chromeの場合はchromeから通知の許可を表示できるよう設定を変える。
 */





const task_name_list_test = ["プッシュ通知の実装","宿題","レポート"]// テスト用

function requestPushPermission() {
    Push.create("許可が必要です", {
        body: "プッシュ通知を受け取るために許可が必要です。",
        timeout: 4000, // 通知が消えるまでの時間 (ミリ秒)
        onClick: function () {
            window.focus();
            this.close();
        }
    });
}

function getTaskNameList (task_name_list) {
    task_name_list = document.getElementsByClassName('name');
    return task_name_list;
}

function getTaskDeadlineList (task_deadline_list) {
    task_deadline_list = document.getElementsByClassName('deadline');
    return task_deadline_list;
}

function sendPushNotification () {// 通知を送信する関数 6時間、1時間、30分、10分、5分、3分
    const task_name_list = []
    const task_deadline_list = []

    getTaskNameList(task_name_list);
    getTaskDeadlineList(task_deadline_list);

    for (var j=0; j < task_name_list.length; j++) {
        if (convert_remaining_time(task_deadline_list[j]) == "6時間") {
            Push.create("アクション通知", {
                body: task_name_list[j] + "の期限が迫っています！",
                timeout: 1000,
                onClick: function () {
                    window.focus();
                    this.close();
                }
            });
        }

        if (convert_remaining_time(task_deadline_list[j])  == "1時間") {
            Push.create("アクション通知", {
                body: task_name_list[j] + "の期限が迫っています！",
                timeout: 1000,
                onClick: function () {
                    window.focus();
                    this.close();
                }
            });
        }

        if (convert_remaining_time(task_deadline_list[j]) == "30分") {
            Push.create("アクション通知", {
                body: task_name_list[j] + "の期限が迫っています！",
                timeout: 1000,
                onClick: function () {
                    window.focus();
                    this.close();
                }
            });
        }

        if (convert_remaining_time(task_deadline_list[j]) == "10分") {
            Push.create("アクション通知", {
                body: task_name_list[j] + "の期限が迫っています！",
                timeout: 1000,
                onClick: function () {
                    window.focus();
                    this.close();
                }
            });
        }

        if (convert_remaining_time(task_deadline_list[j]) == "5分") {
            Push.create("アクション通知", {
                body: task_name_list[j] + "の期限が迫っています！",
                timeout: 1000,
                onClick: function () {
                    window.focus();
                    this.close();
                }
            });
        }

        if (convert_remaining_time(task_deadline_list[j]) == "3分") {
            Push.create("アクション通知", {
                body: task_name_list[j] + "の期限が迫っています！",
                timeout: 1000,
                onClick: function () {
                    window.focus();
                    this.close();
                }
            });
        }
    }
}



setInterval(() => sendPushNotification(), 1000); // 2秒毎に通知を送信