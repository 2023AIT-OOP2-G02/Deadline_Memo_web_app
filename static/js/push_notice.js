/**
 * MacOSの場合、左上のシステム設定から集中モード、おやすみモードをoffにする。
 * 通知の設定から使用するブラウザの通知をonにしておく
 * Chromeの場合はchromeから通知の許可を表示できるよう設定を変える。
 */





const task_name_list = ["プッシュ通知の実装","宿題","レポート"]// テスト用
const invalid_notification = [];// 一度表示した通知のタスク名を格納する配列
const isInvalid = true;// 通知が無効であるかの確認

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

// 通知を送信する関数をボタンのクリックイベントに結びつける
document.getElementById('notifyButton').addEventListener('click', function() {
    if (Push.Permission.has() && !isIOS()) {
        Push.create("通知", {
            body: "これは標準のプッシュ通知です。",
            // その他のオプション
        });
    } else {
        // iOSデバイスの場合のフォールバック通知処理
        alert("iOSデバイスではプッシュ通知がサポートされていません。");
    }
    
    function isIOS() {
        return /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
    }
});

function sendPushNotification (task_name_list) {// 通知を送信する関数
    for (var j=0; j < task_name_list.length; j++) {
        if (checkIsInvalid(task_name_list[j]) == false) {
            invalid_notification.push(task_name_list[j]);
            Push.create("アクション通知", {
                body: task_name_list[j] + "の期限が迫っています！",
                timeout: 1000,
                onClick: function () {
                    console.log('一定時間が経過しました！');
                    this.close();
                }
            });
        }
    }
}

function checkIsInvalid (task_name) { //タスク名が該当するかチェック
    for(var i=0; i < invalid_notification.length; i++) {
        if (task_name == invalid_notification[i]) {
            return true;
        }
    }
    return false;
}

function refreshList() {
    //ここは都合のいい条件でクリアするように変更してOK
    invalid_notification.splice(0,1)
}

setInterval(refreshList, 5000);
setInterval(() => sendPushNotification(task_name_list), 2000); // 2秒毎に通知を送信