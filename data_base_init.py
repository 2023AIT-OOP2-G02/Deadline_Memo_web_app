from flask import Flask, request, render_template, jsonify, Blueprint
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_startup import app

app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# データベース
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.String(50), primary_key=True)  # 課題識別用のID
    title = db.Column(db.String(120))
    deadline = db.Column(db.DateTime)
    subject = db.Column(db.String(120))
    star_num = db.Column(db.Integer)
    memo = db.Column(db.String(2000))
    memo_img = db.Column(db.String(120))  # メモの画像のファイル名をuuidで保存
    created_by = db.Column(db.String(120))
    created_at = db.Column(db.DateTime,
                        default=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))))  # 作成日時(日本時間)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))),
                        onupdate=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))))  # 更新日時(日本時間)


with app.app_context():
    db.drop_all()  # データベースの全てのテーブルを削除
    db.create_all()  # データベースのテーブルを再作成

