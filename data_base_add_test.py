from data_base_init import Data, db, app
from DataAccess import DataAccess

# for debug
if __name__ == "__main__":
    data_json = '''{
        "fDja8VuaVy4BGNfXDi1gha": {
            "title": "test1",
            "deadline": "2022-02-20 00:00:00",
            "subject": "オブ演",
            "memo": "感想いっぱい書く必要",
            "memo_img": "img/mCpcLbPq6pGf4ztYZsrKQi.jpg",
            "created_at": "2021-01-02 00:00:00",
            "updated_at": "2021-01-02 00:00:00",
            "created_by": "32ce6c36-5aeb-4a44-871c-209e14cbd272"
        }
    }'''

    with app.app_context():
        DataAccess.add_data(data_json)

        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().title)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().deadline)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().subject)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().memo)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().memo_img)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().created_at)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().updated_at)
        print(Data.query.filter_by(id='fDja8VuaVy4BGNfXDi1gha').first().created_by)

    pass
