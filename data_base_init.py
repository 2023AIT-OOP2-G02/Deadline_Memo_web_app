# main.pyに移動
#
# from flask_sqlalchemy import SQLAlchemy
#
# # from main import app
#
# app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく
#
# # データベース
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
# db = SQLAlchemy(app)
#
# if __name__ == "__main__":
#     # debugモードが不要の場合は、debug=Trueを消してください
#     # app.run(debug=True)
#
#     with app.app_context():
#         db.drop_all()  # データベースの全てのテーブルを削除
#         db.create_all()  # データベースのテーブルを再作成
#
#     pass
