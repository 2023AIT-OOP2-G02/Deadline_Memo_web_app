import json
from datetime import datetime

from data_base_init import db, Data

class DataAccess:
    def add_data(data_json: str): # 例外処理が必要かも
        data_dict = json.loads(data_json)
        
        id          :str        = list(data_dict.keys())[0]
        title       :str        = data_dict[id]["title"]
        deadline    :datetime   = datetime.strptime(data_dict[id]["deadline"], '%Y-%m-%d %H:%M:%S')
        subject     :str        = data_dict[id]["subject"]
        memo        :str        = data_dict[id]["memo"]
        memo_img    :str        = data_dict[id]["memo_img"]
        created_at  :datetime   = datetime.strptime(data_dict[id]["created_at"], '%Y-%m-%d %H:%M:%S') # この値は使わない
        updated_at  :datetime   = datetime.strptime(data_dict[id]["updated_at"], '%Y-%m-%d %H:%M:%S') # この値は使わない
        created_by  :str        = data_dict[id]["created_by"] # user_id
        
        # データベースにデータを追加
        data = Data(id=id, title=title, deadline=deadline, subject=subject, memo=memo, memo_img=memo_img, created_by=created_by)
        db.session.add(data)
        db.session.commit()
        
    def delete_data(id: str):
        data = Data.query.filter_by(id=id).first()
        if data:
            db.session.delete(data)
            db.session.commit()
            
    def update_data(data_json: str): # 例外処理が必要かも
        data_dict = json.loads(data_json)
        
        id          :str        = list(data_dict.keys())[0]
        title       :str        = data_dict[id]["title"]
        deadline    :datetime   = datetime.strptime(data_dict[id]["deadline"], '%Y-%m-%d %H:%M:%S')
        subject     :str        = data_dict[id]["subject"]
        memo        :str        = data_dict[id]["memo"]
        memo_img    :str        = data_dict[id]["memo_img"]
        created_at  :datetime   = datetime.strptime(data_dict[id]["created_at"], '%Y-%m-%d %H:%M:%S') # この値は使わない
        updated_at  :datetime   = datetime.strptime(data_dict[id]["updated_at"], '%Y-%m-%d %H:%M:%S') # この値は使わない
        created_by  :str        = data_dict[id]["created_by"] # user_id
        
        data = Data.query.filter_by(id=id).first()
        if data:
            data.title      = title
            data.deadline   = deadline
            data.subject    = subject
            data.memo       = memo
            data.memo_img   = memo_img
            data.created_by = created_by
            db.session.commit()
            
    def fetch_data_all(user_id: str) -> str: # json形式で返す
        data_dict = {}
        data_list = Data.query.filter_by(created_by=user_id).all()
        for data in data_list:
            data_dict[data.id] = {
                "title"     : data.title,
                "deadline"  : data.deadline.strftime('%Y-%m-%d %H:%M:%S'),
                "subject"   : data.subject,
                "memo"      : data.memo,
                "memo_img"  : data.memo_img,
                "created_at": data.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": data.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                "created_by": data.created_by
            }
        return json.dumps(data_dict, ensure_ascii=False)