import random
import threading
from data_base_init import Data, db
from flask_startup import app
from flask import Flask, request, render_template, jsonify, Blueprint
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

from DataAccess import DataAccess
from generate_id import generate_id


# http://127.0.0.1:5000/
@app.route('/')
def index():



@app.route("/add_page")
def add_page():
    return render_template("add_page.html")


@app.route("/add_data")  # TODO: 仮データの部分を削除する時、methods=["POST"]をつける
def add_data():
    # データを追加する関数 #

    # 課題IDを発行
    kadai_id = generate_id()

    # 仮データ
    # POSTによって送られてくるデータに課題IDを添える
    temp_data_json = f'''{{
        "{kadai_id}": {{
            "title": "課題番号{random.randint(0, 100)}",
            "deadline": "2022-02-20 00:00:00",
            "subject": "オブ演",
            "memo": "感想いっぱい書く必要",
            "memo_img": "img/mCpcLbPq6pGf4ztYZsrKQi.jpg",
            "created_at": "2021-01-02 00:00:00",
            "updated_at": "2021-01-02 00:00:00",
            "created_by": "test_user1"
        }}
    }}'''

    print(temp_data_json)

    # データをDBに追加
    DataAccess.add_data(temp_data_json)

    # DBに正常に追加されていることを確認
    # TODO: user_idも表示する
    print(f"kadai_id: {kadai_id}")
    print(f"title: {Data.query.filter_by(id=kadai_id).first().title}")

    return render_template("add_page.html") # これも仮


@app.route("/detail_edit_page")
def detail_edit_page():
    return render_template("detail_edit_page.html")


@app.route("/remove_page")
def remove_page():
    return render_template("remove_page.html")


@app.route("/search_page")
def search_page():
    return render_template("search_page.html")


# for debug
@app.route("/API_test_DatabaseAdd")
def API_test_DatabaseAdd():
    return render_template("API_test_DatabaseAdd.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)
