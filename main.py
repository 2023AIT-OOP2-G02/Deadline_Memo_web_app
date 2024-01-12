import threading

from flask import Flask, request, render_template, jsonify, Blueprint
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する



app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく


# http://127.0.0.1:5000/
@app.route('/')
def index():

    return render_template("index.html")

@app.route("/add_page", methods=["GET"])
def add_page():
    return render_template("add_page.html")

@app.route("/detail_edit_page", methods=["GET"])
def detail_edit_page():
    return render_template("detail_edit_page.html")

@app.route("/remove_page", methods=["GET"])
def remove_page():
    return render_template("remove_page.html")

@app.route("/search_page", methods=["GET"])
def search_page():
    return render_template("search_page.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)
