from flask import Flask, request, render_template, jsonify, Blueprint
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

import datetime
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# データベース
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))))
    
with app.app_context():
    db.drop_all()  # データベースの全てのテーブルを削除
    db.create_all()  # データベースのテーブルを再作成

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    # app.run(debug=True)
    pass
