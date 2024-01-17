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
    Push.create("アクション通知", {
        body: "ボタンがクリックされました！",
        timeout: 5000,
        onClick: function () {
            console.log('通知がクリックされました！');
            this.close();
        }
    });
});