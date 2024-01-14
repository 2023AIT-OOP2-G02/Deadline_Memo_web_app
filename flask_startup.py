from flask import Flask, request, render_template, jsonify, Blueprint

# main.pyとdata_base_initの循環importを防ぐために、
# appをここからimportする

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく
