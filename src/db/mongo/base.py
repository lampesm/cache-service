from decouple import config
from  motor.motor_asyncio import AsyncIOMotorClient


async def insert_to_db(my_dict) -> None:
    conn_str = f"mongodb://{config('MONGO_INITDB_ROOT_USERNAME')}:{config('MONGO_INITDB_ROOT_PASSWORD')}@mongo:27017/{config('MONGO_INITDB_DATABASE')}?authSource=admin"
    client = AsyncIOMotorClient(conn_str)
    db = client[config('MONGO_INITDB_DATABASE')]
    wiki_collection = db["wikipedia"]
    await wiki_collection.insert_one(my_dict)
