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
    const now_sec = Number(Date().split(/[ :]/)[6]);
    if (deadline === "6時間" && now_sec === 1) {
        Push.create("Deadline Tracker", {
            body: `「${title}」の期限は残り6時間です！`,
            timeout: 5000,
            onClick: function () {
                window.focus();
                this.close();
            }
        });
    }

    if (deadline === "1時間" && now_sec === 1) {
        Push.create("Deadline Tracker", {
            body: `「${title}」の期限は残り1時間です！`,
            timeout: 5000,
            onClick: function () {
                window.focus();
                this.close();
            }
        });
    }

    if (deadline === "30分") {
        Push.create("Deadline Tracker", {
            body: `「${title}」の期限は残り30分です！`,
            timeout: 5000,
            onClick: function () {
                window.focus();
                this.close();
            }
        });
    }

    if (deadline === "10分") {
        Push.create("Deadline Tracker", {
            body: `「${title}」の期限は残り10分です！`,
            timeout: 5000,
            onClick: function () {
                window.focus();
                this.close();
            }
        });
    }

    if (deadline === "3分") {
        Push.create("Deadline Tracker", {
            body: `「${title}」の期限は残り3分です！`,
            timeout: 5000,
            onClick: function () {
                window.focus();
                this.close();
            }
        });
    }
}



//setInterval(() => sendPushNotification(), 1000); // 1秒毎に通知を送信