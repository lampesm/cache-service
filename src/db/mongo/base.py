from pprint import pprint

from decouple import config
from motor.motor_asyncio import AsyncIOMotorClient


class MongoManager:
    def __init__(self) -> None:
        conn_str = f"mongodb://{config('MONGO_INITDB_ROOT_USERNAME')}:{config('MONGO_INITDB_ROOT_PASSWORD')}@mongo:27017/{config('MONGO_INITDB_DATABASE')}?authSource=admin"
        self.client = AsyncIOMotorClient(conn_str)
        self.db = self.client[config("MONGO_INITDB_DATABASE")]
        self.wiki_collection = self.db["wikipedia"]

    async def insert_to_db(self, my_dict) -> None:
        await self.wiki_collection.insert_one(my_dict)
    
    @property
    async def do_find_one(self) -> None:
        document = await self.db.wiki_collection.find_one({'i': {'$lt': 1}})
        pprint(f"results: {document}")
    
    @property
    def close_mongodb(self):
        self.client.close()
