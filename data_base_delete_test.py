from data_base_init import db, app
from DataAccess import DataAccess, Data

if __name__ == "__main__":
    with app.app_context():
        DataAccess.delete_data(id='fDja8VuaVy4BGNfXDi1gha')
