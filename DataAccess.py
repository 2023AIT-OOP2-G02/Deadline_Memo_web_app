import json
from datetime import datetime
import random

from data_base_init import db, Data


# DBをマネジメントするクラス
class DataAccess:

    # データを追加する関数
    def add_data(data_json: str):  # 例外処理が必要かも
        """データベースにデータを追加する関数

        Args:
            data_json (str): json形式のデータ
        """
        
        try:
            data_dict = json.loads(data_json)
        except json.decoder.JSONDecodeError as e:
            raise e

        id: str = list(data_dict.keys())[0]
        title: str = data_dict[id]["title"]
        deadline: datetime = datetime.strptime(data_dict[id]["deadline"], '%Y-%m-%d %H:%M:%S')
        subject: str = data_dict[id]["subject"]
        star_num: int = data_dict[id]["star_num"]
        memo: str = data_dict[id]["memo"]
        memo_img: str = data_dict[id]["memo_img"]
        created_at: datetime = datetime.strptime(data_dict[id]["created_at"], '%Y-%m-%d %H:%M:%S')  # この値は使わない
        updated_at: datetime = datetime.strptime(data_dict[id]["updated_at"], '%Y-%m-%d %H:%M:%S')  # この値は使わない
        created_by: str = data_dict[id]["created_by"]  # user_id

        # データベースにデータを追加
        data = Data(id=id, title=title, deadline=deadline, subject=subject, star_num = star_num, memo=memo, memo_img=memo_img,
                    created_by=created_by)
        db.session.add(data)
        db.session.commit()
        db.session.close()

    # 単独のデータを削除する関数
    def delete_data(id: str):
        """データベースからデータを削除する関数

        Args:
            id (str): 課題ID
        """
        
        data = Data.query.filter_by(id=id).first()
        if data:
            db.session.delete(data)
            db.session.commit()
            
            
    # 複数のデータを削除する関数
    def delete_data_list(id_list: list):
        """データベースからデータを削除する関数

        Args:
            id_list (list): 課題IDのリスト
        """
        
        for id in id_list:
            data = Data.query.filter_by(id=id).first()
            if data:
                db.session.delete(data)
        db.session.commit()


    # データを更新する関数
    def update_data(data_json: str):  # 例外処理が必要かも
        """データベースのデータを更新する関数\n
            課題IDが同じものを更新します
        Args:
            data_json (str): json形式のデータ
        """
        try:
            data_dict = json.loads(data_json)
        except json.decoder.JSONDecodeError as e:
            raise e
            

        id: str = list(data_dict.keys())[0]
        title: str = data_dict[id]["title"]
        deadline: datetime = datetime.strptime(data_dict[id]["deadline"], '%Y-%m-%d %H:%M:%S')
        subject: str = data_dict[id]["subject"]
        star_num: int = data_dict[id]["star_num"]
        memo: str = data_dict[id]["memo"]
        memo_img: str = data_dict[id]["memo_img"]
        created_at: datetime = datetime.strptime(data_dict[id]["created_at"], '%Y-%m-%d %H:%M:%S')  # この値は使わない
        updated_at: datetime = datetime.strptime(data_dict[id]["updated_at"], '%Y-%m-%d %H:%M:%S')  # この値は使わない
        created_by: str = data_dict[id]["created_by"]  # user_id

        data = Data.query.filter_by(id=id).first()
        if data:
            data.title = title
            data.deadline = deadline
            data.subject = subject
            data.star_num = star_num
            data.memo = memo
            data.memo_img = memo_img
            data.created_by = created_by
            db.session.commit()


    # データを取得する関数
    def fetch_data_all(user_id: str) -> str:  # json形式で返す
        """指定したユーザーのデータを全て取得する関数

        Args:
            user_id (str): ユーザーID

        Returns:
            str: json形式のデータ
        """
        
        data_dict = {}
        data_list = Data.query.filter_by(created_by=user_id).all()
        for data in data_list:
            data_dict[data.id] = {
                "title": data.title,
                "deadline": data.deadline.strftime('%Y-%m-%d %H:%M:%S'),
                "subject": data.subject,
                "star_num": data.star_num,
                "memo": data.memo,
                "memo_img": data.memo_img,
                "created_at": data.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": data.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                "created_by": data.created_by
            }
        return json.dumps(data_dict, ensure_ascii=False)
    
    
    def fetch_AllUser_data() -> str:  # json形式で返す
        """全てのユーザーのデータを取得する関数

        Returns:
            str: json形式のデータ
        """
        data_dict = {}
        data_list = Data.query.all()
        for data in data_list:
            data_dict[data.id] = {
                "title": data.title,
                "deadline": data.deadline.strftime('%Y-%m-%d %H:%M:%S'),
                "subject": data.subject,
                "star_num": data.star_num,
                "memo": data.memo,
                "memo_img": data.memo_img,
                "created_at": data.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": data.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                "created_by": data.created_by
            }
        return json.dumps(data_dict, ensure_ascii=False)
    
    
    # ランダムに1つ課題IDを取得
    def random_fetch_id() -> str:
        """データベース内からランダムに1つ課題IDを取得する関数

        Returns:
            str: 課題ID
        """
        
        
        data_list = Data.query.all()
        data = data_list[random.randint(0, len(data_list) - 1)]
        return data.id


    # process
    
    def search_data_json(data_json:str, title= None, deadline_date = None, subject = None, star_num = None) -> str: # json形式で返す
        """jsonデータから条件に合うデータを抽出する関数

        Args:
            data_json (str): json形式のデータ
            title (str): 課題のタイトル. Defaults to None.
            deadline_date (str): 締切日. Defaults to None.
            subject (str): 講義名. Defaults to None.
            star_num (int): 重要度. Defaults to None.

        Returns:
            str: json形式のデータ
        """
        
        if data_json == None:
            return None
        
        data_dict = json.loads(data_json)
        
        if title:
            data_dict = {k: v for k, v in data_dict.items() if title in v["title"]}
            
        if deadline_date:
            data_dict = {k: v for k, v in data_dict.items() if deadline_date in v["deadline"]}
            
        if subject:
            data_dict = {k: v for k, v in data_dict.items() if subject in v["subject"]}
            
        if star_num:
            star_num = int(star_num)
            data_dict = {k: v for k, v in data_dict.items() if star_num == v["star_num"]}
            
        return json.dumps(data_dict, ensure_ascii=False)
    
    
    def sort_data_json(data_json:str, sort_key: str, order: str) -> str: # json形式で返す
        """jsonデータをソートする関数

        Args:
            data_json (str): json形式のデータ
            sort_key (str): sortするキー
            order (str): 昇順(up)か降順(down)か

        Returns:
            str: json形式のデータ
        """
        
        if data_json == None:
            return None
        
        data_dict = json.loads(data_json)
        
        if sort_key and order:
            reverse = False
            if order == "down":
                reverse = True
            if sort_key == "deadline" or sort_key == "created_at":
                data_dict = sorted(data_dict.items(), key=lambda x:datetime.strptime(x[1][sort_key], '%Y-%m-%d %H:%M:%S'), reverse=reverse)
            else:
                data_dict = sorted(data_dict.items(), key=lambda x:x[1][sort_key], reverse=reverse)
            
        
        return json.dumps(dict(data_dict), ensure_ascii=False)