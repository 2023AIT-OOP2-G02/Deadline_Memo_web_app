import datetime
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
    return render_template("index.html")


@app.route("/add_page")
def add_page():
    return render_template("add_page.html")


@app.route("/add_data", methods=["POST"])  # TODO: 仮データの部分を削除する時、methods=["POST"]をつける
def add_data():
    # 課題追加ボタン #

    # 検索パラメータの取得
    title = request.form.get('title', None)
    deadline = request.form.get('deadline', None)
    subject = request.form.get('subject', None)
    memo = request.form.get('memo', None)
    star_num = request.form.get('star_num', None)

    # デバッグ用
    print(f"title: {title}")
    print(f"deadline: {deadline}")
    print(f"subject: {subject}")
    print(f"memo: {memo}")
    print(f"star_num: {star_num}")

    # エラー用のメッセージを格納する変数
    message = ""

    # 存在しない場合、返すメッセージを増やす
    if title == "":
        message += "titleが未入力です。\n"
    if deadline == "":
        message += "deadlineが未入力です。\n"
    if subject == "":
        message += "subjectが未入力です。\n"
    if subject == "":
        memo += "memoが未入力です。\n"
    if star_num == "":
        message += "star_numが未入力です。\n"

    if len(message) > 0:
        return jsonify({
            "error": message
        })

    # 課題IDを発行
    kadai_id = generate_id()

    # コンマ秒を省いた現在時刻を取得
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # POSTによって送られてくるデータに課題IDを添える
    # TODO: memo_imgを追加する
    # TODO: created_byを追加する
    # TODO: deadlineの時刻を省く(DBが受け取る構造を変更する)
    data_json = f'''{{
        "{kadai_id}": {{
            "title": "{title}",
            "deadline": "{deadline} 00:00:00",
            "subject": "{subject}",
            "memo": "{memo}",
            "memo_img": "testdayo.jpg",
            "created_at": "{now}",
            "updated_at": "{now}",
            "created_by": "test_user1"
        }}
    }}'''

    print(data_json)

    # データをDBに追加
    DataAccess.add_data(data_json)

    # DBに正常に追加されていることを確認
    # TODO: user_idも表示する
    print("以下のデータの追加を確認：")
    print(f"kadai_id: {kadai_id}")
    print(f"title: {Data.query.filter_by(id=kadai_id).first().title}")


    # 送信が完了したらTOPページに戻る
    return render_template("index.html")


@app.route("/detail_edit_page")
def detail_edit_page():
    return render_template("detail_edit_page.html")


@app.route("/detail_edit_data")
def detail_edit_data():
    # 課題編集確定ボタン #
    return render_template("index.html")


@app.route("/remove_page")
def remove_page():
    return render_template("remove_page.html")


@app.route("/remove_data")
def remove_data():
    # 課題削除ボタン #
    return render_template("index.html")



@app.route("/search_page")
def search_page():
    return render_template("search_page.html")


@app.route("/search_data")
def search_data():
    # 課題検索ボタン #

    return render_template("index.html")



if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)
