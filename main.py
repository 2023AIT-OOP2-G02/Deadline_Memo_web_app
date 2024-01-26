import datetime
import random
import threading
from data_base_init import Data, db
from flask_startup import app
from flask import Flask, request, render_template, jsonify, Blueprint, url_for, redirect
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

from DataAccess import DataAccess
from generate_id import generate_id


@app.route('/')
def index():
    return render_template("fetch_top_page.html")


@app.route("/fetch_top_data", methods=["POST"])
def fetch_my_all_data():
    user_id = request.values['userID']
    print(user_id)
    return jsonify({'redirect': url_for("render_top_data", user_id=user_id)})


# http://127.0.0.1:5000/
@app.route('/render_top_data/<user_id>')
def render_top_data(user_id):
    res = DataAccess.fetch_data_all(user_id)
    # res = DataAccess.fetch_data_all(user_id = user_id)
    data_dict = json.loads(res)
    keys = list(data_dict.keys())
    return render_template("index.html", keys=keys, data_dict=data_dict)


@app.route('/remove_page')
def remove_page():
    return render_template("fetch_remove_page.html")


@app.route("/fetch_remove_data", methods=["POST"])
def fetch_my_all_remove_data():
    user_id = request.values['userID']
    print(user_id)
    return jsonify({'redirect': url_for("render_remove_data", user_id=user_id)})


# http://127.0.0.1:5000/
@app.route('/render_remove_data/<user_id>')
def render_remove_data(user_id):
    res = DataAccess.fetch_data_all(user_id)
    # res = DataAccess.fetch_data_all(user_id = user_id)
    data_dict = json.loads(res)
    keys = list(data_dict.keys())
    return render_template("remove_page.html", keys=keys, data_dict=data_dict)


@app.route("/remove_data", methods=["POST"])
def remove_data():
    # 課題削除ボタン #
    # 削除する課題IDのリストを取得
    user_id = request.form.get('created_by', None)
    remove_ids = request.form.getlist('remove_ids')
    print(user_id)
    # DBから削除
    DataAccess.delete_data_list(remove_ids)
    # 削除通知する
    res = DataAccess.fetch_data_all(user_id)
    data_dict = json.loads(res)
    keys = list(data_dict.keys())
    notice = "データの削除が完了しました。"
    return render_template("index.html", keys=keys, data_dict=data_dict, notice=notice)


# res = DataAccess.fetch_data_all("32ce6c36-5aeb-4a44-871c-209e14cbd272")

@app.route("/add_page")
def add_page():
    return render_template("add_page.html")


@app.route("/add_data", methods=["POST"])
def add_data():
    # 課題追加ボタン #

    # 検索パラメータの取得
    title = request.form.get('title', None)
    deadline_date = request.form.get('deadline_date', None)
    deadline_time = request.form.get('deadline_time', None)
    subject = request.form.get('subject', None)
    memo = request.form.get('memo', None)
    star_num = request.form.get('star_num', None)
    created_by = request.form.get('created_by', None)

    # デバッグ用
    print(f"title: {title}")
    print(f"deadline_date: {deadline_date}")
    print(f"deadline_time: {deadline_time}")
    print(f"subject: {subject}")
    print(f"memo: {memo}")
    print(f"star_num: {star_num}")
    print(f"created_by: {created_by}")

    # エラー用のメッセージを格納する変数
    message = ""

    # 存在しない場合、返すメッセージを増やす
    if title == "":
        message += "titleが未入力です。\n"
    if deadline_date == "":
        message += "deadline_dateが未入力です。\n"
    if deadline_time == "":
        message += "deadline_timeが未入力です。\n"
    if subject == "":
        message += "subjectが未入力です。\n"
    if memo == "":
        memo += "memoが未入力です。\n"
    if star_num == "":
        message += "star_numが未入力です。\n"
    if created_by == "":
        message += "created_byが未入力です。\n"

    if len(message) > 0:
        return jsonify({
            "error": message
        })

    # 課題IDを発行
    kadai_id = generate_id()

    # コンマ秒を省いた現在時刻を取得
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    row_data_dict = {
        "title": title,
        "deadline": f"{deadline_date} {deadline_time}:00",
        "subject": subject,
        "star_num": star_num,
        "memo": memo,
        "memo_img": "testdayo.jpg",
        "created_at": now,
        "updated_at": now,
        "created_by": created_by
    }
    row_data_dict = {kadai_id: row_data_dict}

    # POSTによって送られてくるデータに課題IDを添える
    # TODO: memo_imgを追加する
    # data_json = f'''{{
    #     "{kadai_id}": {{
    #         "title": "{title}",
    #         "deadline": "{deadline_date} {deadline_time}:00",
    #         "subject": "{subject}",
    #         "star_num": {star_num},
    #         "memo": "{memo}",
    #         "memo_img": "testdayo.jpg",
    #         "created_at": "{now}",
    #         "updated_at": "{now}",
    #         "created_by": "{created_by}"
    #     }}
    # }}'''

    # 適切なjson形式に変換
    data_json = json.dumps(row_data_dict)
    # print(data_json)

    # データをDBに追加
    try:
        DataAccess.add_data(data_json)
    except json.decoder.JSONDecodeError:
        user_id = request.form.get('created_by', None)
        res = DataAccess.fetch_data_all(user_id)
        data_dict = json.loads(res)
        keys = list(data_dict.keys())
        return render_template("index.html", data_dict=data_dict, keys=keys, error="データの登録に失敗しました。")

    # DBに正常に追加されていることを確認
    print("以下のデータの追加を確認：")
    print(f"kadai_id: {kadai_id}")
    print(f"title: {Data.query.filter_by(id=kadai_id).first().title}")

    user_id = request.form.get('created_by', None)
    res = DataAccess.fetch_data_all(user_id)
    data_dict = json.loads(res)
    keys = list(data_dict.keys())
    notice = "データの登録が完了しました。"
    # 送信が完了したらTOPページに戻る
    return render_template("index.html", data_dict=data_dict, keys=keys, notice=notice)


@app.route("/detail_edit_page/<kadai_id>", methods=["GET"])
def detail_edit_page(kadai_id):
    kadai = Data.query.get(kadai_id)
    return render_template("detail_edit_page.html", kadai=kadai)


@app.route("/detail_edit_data", methods=["POST"])
def detail_edit_data():
    # 課題編集確定ボタン #
    # 検索パラメータの取得
    title = request.form.get('title', None)
    deadline_date = request.form.get('deadline_date', None)
    deadline_time = request.form.get('deadline_time', None)
    subject = request.form.get('subject', None)
    memo = request.form.get('memo', None)
    star_num = request.form.get('star_num', None)
    created_by = request.form.get('created_by', None)
    kadai_id = request.form.get('kadai_id', None)
    created_at = request.form.get('created_at', None)

    # デバッグ用
    # print(f"title: {title}")
    # print(f"deadline_date: {deadline_date}")
    # print(f"deadline_time: {deadline_time}")
    # print(f"subject: {subject}")
    # print(f"memo: {memo}")
    # print(f"star_num: {star_num}")
    # print(f"created_by: {created_by}")

    # エラー用のメッセージを格納する変数
    message = ""

    # 存在しない場合、返すメッセージを増やす
    if title == "":
        message += "titleが未入力です。\n"
    if deadline_date == "":
        message += "deadline_dateが未入力です。\n"
    if deadline_time == "":
        message += "deadline_timeが未入力です。\n"
    if subject == "":
        message += "subjectが未入力です。\n"
    if subject == "":
        memo += "memoが未入力です。\n"
    if star_num == "":
        message += "star_numが未入力です。\n"
    if created_by == "":
        message += "created_byが未入力です。\n"

    if len(message) > 0:
        return jsonify({
            "error": message
        })

    # コンマ秒を省いた現在時刻を取得
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # created_atのコンマ秒を省く
    created_at = created_at.split(".")[0]
    # deadlineの:が2つあるときに、:を1つにする
    deadline_time_split = deadline_time.split(":")
    if len(deadline_time_split) == 3:
        deadline_time = f"{deadline_time_split[0]}:{deadline_time_split[1]}"

    # データの整形
    row_data_dict = {
        "title": title,
        "deadline": f"{deadline_date} {deadline_time}:00",
        "subject": subject,
        "star_num": star_num,
        "memo": memo,
        "memo_img": "testdayo.jpg",
        "created_at": now,
        "updated_at": now,
        "created_by": created_by
    }
    row_data_dict = {kadai_id: row_data_dict}

    # 適切なjson形式に変換
    data_json = json.dumps(row_data_dict)
    # print(data_json)

    # DBのデータを更新
    try:
        DataAccess.update_data(data_json)
    except json.decoder.JSONDecodeError:
        user_id = request.form.get('created_by', None)
        res = DataAccess.fetch_data_all(user_id)
        data_dict = json.loads(res)
        keys = list(data_dict.keys())
        return render_template("index.html", data_dict=data_dict, keys=keys, error="データの登録に失敗しました。")

    # DBに正常に反映されていることを確認
    # print("以下のデータの追加を確認：")
    # print(f"kadai_id: {kadai_id}")
    # print(f"title: {Data.query.filter_by(id=kadai_id).first().title}")

    user_id = request.form.get('created_by', None)
    res = DataAccess.fetch_data_all(user_id)
    data_dict = json.loads(res)
    keys = list(data_dict.keys())
    notice = "データの更新が完了しました。"

    # 送信が完了したらTOPページに戻る
    return render_template("index.html", keys=keys, data_dict=data_dict, notice=notice)


# @app.route("/remove_page")
# def remove_page():
#     return render_template("remove_page.html")


@app.route("/search_page")
def search_page():
    return render_template("search_page.html")


@app.route("/sort_page")
def sort_page():
    return render_template("sort_page.html")


@app.route("/search_data", methods=["POST"])
def search_data():
    # 課題検索ボタン #
    title = request.form.get('title', None)
    deadline_date = request.form.get('deadline_date', None)
    subject = request.form.get('subject', None)
    star_num = request.form.get('star_num', None)
    user_id = request.form.get('created_by', None)

    data_json = DataAccess.fetch_data_all(user_id=user_id)
    res_json = DataAccess.search_data_json(data_json=data_json,
                                           title=title, deadline_date=deadline_date, subject=subject, star_num=star_num)

    # # for debug
    # if title : print(f"title: {title}")
    # if deadline_date : print(f"deadline_date: {deadline_date}")
    # if subject : print(f"subject: {subject}")
    # if star_num : print(f"star_num: {int(star_num)}")
    # print(f"user_id: {user_id}")

    res_dict = json.loads(res_json)
    keys = list(res_dict.keys())
    # 検索条件でfilterしたページを表示
    return render_template("index.html", keys=keys, data_dict=res_dict)


@app.route("/sort_data", methods=["POST"])
def sort_data():
    # 課題並び替えボタン #
    sort_key = request.form.get('sort_key', None)
    order = request.form.get('order', None)
    user_id = request.form.get('created_by', None)

    if sort_key and order:
        data_json = DataAccess.fetch_data_all(user_id=user_id)
        res_json = DataAccess.sort_data_json(
            data_json=data_json, sort_key=sort_key, order=order)
        res_dict = json.loads(res_json)
        keys = list(res_dict.keys())

        # for debug
        print(res_dict)

        # sort条件でsortしたページを表示
        return render_template("index.html", keys=keys, data_dict=res_dict)

    # default
    return render_template("fetch_top_page.html")


@app.route("/fetch_all_data", methods=["POST"])
def fetch_all_data():
    user_id = request.values['userID']

    res = DataAccess.fetch_data_all(user_id=user_id)
    return jsonify(res)


@app.route("/delete_data", methods=["POST"])
def delete_data():
    # データを削除する関数 #

    kadai_id = request.values["kadai_id"]

    # データをDBから削除
    DataAccess.delete_data(kadai_id)

    return 'success'


# for debug
@app.route("/API_test_DatabaseAdd")
def API_test_DatabaseAdd():
    return render_template("API_test_DatabaseAdd.html")


# for debug fetchall:1
@app.route("/API_test_FetchAll")
def API_test_FetchAll():
    res = DataAccess.fetch_data_all(user_id='test_user1')

    data_dict = json.loads(res)
    keys = list(data_dict.keys())
    # print(res)
    return render_template("API_test_FetchAll.html", keys=keys, data_dict=data_dict)


# for debug fetchall:2
@app.route("/API_test_FetchMyData", methods=["POST"])
def API_test_FetchMyData():
    user_id = request.values['userID']
    # print(user_id)
    return jsonify({'redirect': url_for("renderMyData", user_id=user_id)})


# for debug fetchall:3
@app.route('/renderMyData/<user_id>')
def renderMyData(user_id):
    res = DataAccess.fetch_data_all(user_id=user_id)

    data_dict = json.loads(res)
    keys = list(data_dict.keys())
    return render_template("API_test_FetchAll.html", keys=keys, data_dict=data_dict)


# for debug
@app.route("/API_test_DatabaseDelete")
def API_test_DatabaseDelete():
    return render_template("API_test_DatabaseDelete.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    with app.app_context():
        db.drop_all()  # データベースの全てのテーブルを削除
        db.create_all()  # データベースのテーブルを再作成
    app.run(debug=True, port=5050)
