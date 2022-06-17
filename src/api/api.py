from fastapi import FastAPI

from src.crawler.wikipedia import Wikipedia
from src.db.mongo.base import insert_to_db

app = FastAPI()


@app.get("/api/v1/wiki/")
def downalod_wiki_query(query: str):
    w = Wikipedia(query)
    insert_to_db(w.get_information)

    return w.get_information
