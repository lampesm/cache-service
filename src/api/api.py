from fastapi import FastAPI

from src.crawler.wikipedia import Wikipedia
from src.db.mongo.base import MongoManager

app = FastAPI()
mongo = MongoManager()

@app.get("/api/v1/wiki/")
def downalod_wiki_query(query: str):
    wiki = Wikipedia(query)
    wiki_result = wiki.get_information

    if wiki_result:
        mongo.insert_to_db(wiki_result)
    
    mongo.do_find_one
    mongo.close_mongodb

    return wiki_result
