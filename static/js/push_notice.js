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
