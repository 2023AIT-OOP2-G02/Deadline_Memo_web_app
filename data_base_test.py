from flask import Flask, request, render_template, jsonify, Blueprint
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from data_base_init import Data, db
from main import app

with app.app_context():
    db.drop_all()  # データベースの全てのテーブルを削除
    db.create_all()  # データベースのテーブルを再作成
    
    
def add_data(data_json: str):
    
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


# for debug
if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    # app.run(debug=True)
    
    data_json = '''{
        "fDja8VuaVy4BGNfXDL1ghm": {
            "title": "進捗報告作成",
            "deadline": "2021-01-10 00:00:00",
            "subject": "オブ演",
            "memo": "感想いっぱい書く必要",
            "memo_img": "img/mCpcLbPq6pGf4ztYZsrKQi.jpg",
            "created_at": "2021-01-01 00:00:00",
            "updated_at": "2021-01-01 00:00:00",
            "created_by": "test_user"
        }
    }'''
    
    with app.app_context():
        add_data(data_json)
    
    
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDL1ghm').first().title)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDL1ghm').first().deadline)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDL1ghm').first().subject)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDL1ghm').first().memo)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDL1ghm').first().memo_img)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDL1ghm').first().created_at)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDL1ghm').first().updated_at)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDL1ghm').first().created_by)
    
    pass
