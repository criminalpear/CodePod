from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import db, ai_search

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/snippets")
def get_snippets():
    return db.get_all_snippets()

@app.post("/snippets")
async def add_snippet(data: Request):
    body = await data.json()
    db.add_snippet(body["title"], body["language"], body["code"])
    return {"status": "ok"}

@app.post("/search")
async def search_snippets(data: Request):
    body = await data.json()
    return ai_search.search_snippets(body["query"])
