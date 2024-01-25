/**
 * MacOSの場合、左上のシステム設定から集中モード、おやすみモードをoffにする。
 * 通知の設定から使用するブラウザの通知をonにしておく
 * Chromeの場合はchromeから通知の許可を表示できるよう設定を変える。
 */



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


export function sendPushNotification (title, deadline) {// 通知を送信する関数 6時間、1時間、30分、10分、5分、3分
    if (deadline == "6時間") {
        Push.create("アクション通知", {
            body: title + "の期限が迫っています！",
            timeout: 1000,
            onClick: function () {
                window.focus();
                this.close();
            }
        });
    }

    if (deadline == "1時間") {
        Push.create("アクション通知", {
            body: title + "の期限が迫っています！",
            timeout: 1000,
            onClick: function () {
                window.focus();
                this.close();
            }
        });
    }

    if (deadline == "30分") {
        Push.create("アクション通知", {
            body: title + "の期限が迫っています！",
            timeout: 1000,
            onClick: function () {
                window.focus();
                this.close();
            }
        });
    }

    if (deadline == "10分") {
        Push.create("アクション通知", {
            body: title + "の期限が迫っています！",
            timeout: 1000,
            onClick: function () {
                window.focus();
                this.close();
            }
        });
    }

    if (deadline == "5分") {
        Push.create("アクション通知", {
            body: title + "の期限が迫っています！",
            timeout: 1000,
            onClick: function () {
                window.focus();
                this.close();
            }
        });
    }

    if (deadline == "3分") {
        Push.create("アクション通知", {
            body: title + "の期限が迫っています！",
            timeout: 1000,
            onClick: function () {
                window.focus();
                this.close();
            }
        });
    }
}



//setInterval(() => sendPushNotification(), 1000); // 1秒毎に通知を送信