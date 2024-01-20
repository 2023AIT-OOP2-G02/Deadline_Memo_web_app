from data_base_init import Data, db, app
from DataAccess import DataAccess

if __name__ == "__main__":
    with app.app_context():
        res = DataAccess.fetch_data_all(user_id = '32ce6c36-5aeb-4a44-871c-209e14cbd272')
        
        print(res)