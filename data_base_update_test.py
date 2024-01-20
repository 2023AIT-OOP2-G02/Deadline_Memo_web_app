from data_base_init import Data, db, app
from DataAccess import DataAccess

if __name__ == "__main__":
    with app.app_context():
        data_json = '''{
        "fDja8VuaVy4BGNfXDi1gha": {
            "title": "update_test",
            "deadline": "5555-02-20 00:00:00",
            "subject": "update_test",
            "star_num": 3,
            "memo": "update_test",
            "memo_img": "img/mCpcLbPq6pGf4ztYZsrKQi.jpg",
            "created_at": "5555-01-02 00:00:00",
            "updated_at": "5555-01-02 00:00:00",
            "created_by": "32ce6c36-5aeb-4a44-871c-209e14cbd272"
            }
        }'''
    
        DataAccess.update_data(data_json)


        # 確認用
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().title)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().deadline)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().subject)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().star_num)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().memo)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().memo_img)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().created_at)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().updated_at)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().created_by)