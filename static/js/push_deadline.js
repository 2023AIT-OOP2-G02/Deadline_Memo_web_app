//タスクの期限をチェックする関数

function checkTaskDeadline() {
    for (const kadai_id in jsonData) {
        if (jsonData.hasOwnProperty(kadai_id)) {
            const task = jsonData[kadai_id];
            const now = new Date();
            const deadline = new Date(task.deadline);

            // 期限が現在の日時から24時間以内の場合に通知を表示
            if (deadline - now < 24 * 60 * 60 * 1000) {
                Push.create("タスクリマインダー", {
                    body: `${task.title} の期限が近づいています！`,
                    timeout: 4000,
                    onClick: function () {
                        window.focus();
                        this.close();
                    }
                });
            }
        }
    }
}

// タスクの期限をチェック
checkTaskDeadline();