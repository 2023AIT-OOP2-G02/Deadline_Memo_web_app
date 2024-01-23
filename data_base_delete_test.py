from data_base_init import Data, db, app
from DataAccess import DataAccess

if __name__ == "__main__":
    with app.app_context():
        # 単独のデータを削除する場合
        # DataAccess.delete_data(id='fDja8VuaVy4BGNfXDi1gha')

        # 複数のデータを削除する場合
        id_list = ['c587e0977dd048b5bd49d0117553e3c1', '593785e9b61c4a94a983d8e6af13cb46']
        DataAccess.delete_data_list(id_list=id_list)