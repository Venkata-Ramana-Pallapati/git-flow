from fastapi import FastAPI
from fastapi import Body

app = FastAPI()
BOOKS=[
    {'name':'venkat','age':"22","address":"snk"},
    {'name':'raman','age':"23","address":"mrkp"},
    {'name':'raju','age':"22","address":"drnk"}


]


@app.get("/books")  # Correct: Root path
async def read_root():
    return BOOKS


@app.get("/books/{dynamicparm}")
async def read_all_books(dynamicparm :str ):
    for book in BOOKS:
        if book.get('name').casefold()==dynamicparm.casefold():
            return book