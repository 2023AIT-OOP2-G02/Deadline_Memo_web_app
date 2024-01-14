from flask import Flask, request, render_template, jsonify, Blueprint
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from data_base_init import Data, db, app
from DataAccess import DataAccess


# for debug
if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    # app.run(debug=True)
    
    data_json = '''{
        "fDja8VuaVy4BGNfXDi1ghp": {
            "title": "test1",
            "deadline": "2022-02-20 00:00:00",
            "subject": "オブ演",
            "memo": "感想いっぱい書く必要",
            "memo_img": "img/mCpcLbPq6pGf4ztYZsrKQi.jpg",
            "created_at": "2021-01-02 00:00:00",
            "updated_at": "2021-01-02 00:00:00",
            "created_by": "test_user1"
        }
    }'''
    
    with app.app_context():
        DataAccess.add_data(data_json)


        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().title)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().deadline)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().subject)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().memo)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().memo_img)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().created_at)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().updated_at)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().created_by)
    
    pass
