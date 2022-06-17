from decouple import config
from pymongo import MongoClient


def insert_to_db(my_dict) -> None:
    conn_str = f"mongodb://{config('MONGO_INITDB_ROOT_USERNAME')}:{config('MONGO_INITDB_ROOT_PASSWORD')}@mongo:27017/{config('MONGO_INITDB_DATABASE')}?authSource=admin"
    client = MongoClient(conn_str)
    db = client["cache_service_db"]
    mycol = db["wikipedia"]
    mycol.insert_one(my_dict)
