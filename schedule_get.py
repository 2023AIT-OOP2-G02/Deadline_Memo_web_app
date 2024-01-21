import schedule
import time
import json
from datetime import datetime
from data_base_init import db, Data



def fetch_data_all(user_id: str) -> str:  # json形式で返す
        data_dict = {}
        data_list = Data.query.filter_by(created_by=user_id).all()
        for data in data_list:
            data_dict[data.id] = {
                "title": data.title,
                "deadline": data.deadline.strftime('%Y-%m-%d %H:%M:%S'),
                "subject": data.subject,
                "memo": data.memo,
                "memo_img": data.memo_img,
                "created_at": data.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": data.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                "created_by": data.created_by
            }
        return json.dumps(data_dict, ensure_ascii=False)

# 24時間ごとに関数を実行するようにスケジュールを設定
schedule.every(24).hours.do(fetch_data_all)

# プログラムが終了しないようにループ
while True:
    schedule.run_pending()
    time.sleep(1)
