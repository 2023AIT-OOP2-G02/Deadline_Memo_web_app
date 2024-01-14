from flask import Flask, render_template, jsonify
# from data_base_init import db, Data
from DataAccess import DataAccess
from generate_id import generate_id
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# データベース設定 ##################################
# data_base_initから ##############################
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

# DBマネジメントインスタンスを作成
# DataAccess.add_data()ではなく、
# data_access.add_data()として使用する
data_access = DataAccess(db)


###################################################
# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("index.html")


@app.route("/add_page")
def add_page():
    return render_template("add_page.html")


@app.route("/add_data", methods=["POST"])
def add_data():
    # データを追加する関数 #

    # 課題IDを発行
    kadai_id = generate_id()

    # 仮データ
    # POSTによって送られてくるデータに課題IDを添える
    temp_data_json = f'''{ {kadai_id}: {
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

    # データをDBに追加
    data_access.add_data(temp_data_json)

    # DBに正常に追加されていることを確認
    # TODO: user_idも表示する
    print(f"kadai_id: {kadai_id}")
    # print(f"title: {Data.query.filter_by(id='kadai_id').first().title}")

    # return render_template("add_page.html")
    return jsonify({"result": "ok"})


@app.route("/detail_edit_page")
def detail_edit_page():
    return render_template("detail_edit_page.html")


@app.route("/remove_page")
def remove_page():
    return render_template("remove_page.html")


@app.route("/search_page")
def search_page():
    return render_template("search_page.html")


if __name__ == "__main__":
    with app.app_context():
        db.drop_all()  # データベースの全てのテーブルを削除
        db.create_all()  # データベースのテーブルを再作成

    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)
