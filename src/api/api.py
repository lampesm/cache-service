from fastapi import FastAPI
import uvicorn

from src.crawler.wikipedia import Wikipedia

app = FastAPI()


@app.get("/api/v1/wiki/")
def downalod_wiki_query(query: str):
    w = Wikipedia(query)
    return w.get_information
