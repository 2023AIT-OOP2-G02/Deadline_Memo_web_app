from flask import Flask, request, render_template, jsonify, Blueprint
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

import datetime
from flask_sqlalchemy import SQLAlchemy

from data_base_init_test import Data, app, db

with app.app_context():
    db.drop_all()  # データベースの全てのテーブルを削除
    db.create_all()  # データベースのテーブルを再作成
    

    # データベースにデータを追加
    data = Data(id=2)
    db.session.add(data)
    db.session.commit()

    print(Data.query.filter_by(id=2).first())  # データベースの全てのデータを取得


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)
    pass
