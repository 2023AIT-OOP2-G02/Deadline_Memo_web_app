import uuid


# UUIDを生成する関数
def generate_id():
    # uuidを生成
    new_id = str(uuid.uuid4()).replace('-', '' )
    return new_id


if __name__ == "__main__":
    print(generate_id())
