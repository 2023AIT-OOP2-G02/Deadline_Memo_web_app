from data_base_init import Data, db, app
from DataAccess import DataAccess

if __name__ == "__main__":
    with app.app_context():
        DataAccess.delete_data(id = 'fDja8VuaVy4BGNfXDi1gha')