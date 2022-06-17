from fastapi import FastAPI

from src.crawler.wikipedia import Wikipedia
from src.db.mongo.base import insert_to_db

app = FastAPI()


@app.get("/api/v1/wiki/")
async def downalod_wiki_query(query: str):
    wiki = Wikipedia(query)
    await insert_to_db(wiki.get_information)

    return wiki.get_information
