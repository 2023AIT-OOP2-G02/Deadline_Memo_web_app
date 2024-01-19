from flask_startup import app
from DataAccess import DataAccess

if __name__ == "__main__":
    with app.app_context():
        res = DataAccess.random_fetch_userID()
        print(res)