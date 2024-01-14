from data_base_init import db, app
from DataAccess import DataAccess, Data

if __name__ == "__main__":
    with app.app_context():
        res = DataAccess.fetch_data_all(user_id = 'test_user1')
        
        print(res)