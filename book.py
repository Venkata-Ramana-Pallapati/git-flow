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

#QUERY Parameter

@app.get("/books/")
async def read_query(age:str):
    book_to=[]
    for book in BOOKS:
        if book.get('age').casefold()==age.casefold():
            book_to.append(book)
    return book_to


#post 
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)    


#updated  
@app.put("/books/update_book")
async def updated_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('name').casefold()==updated_book.get('name').casefold():
            BOOKS[i]=updated_book


#delete http request method
@app.delete("/books/delete_book/{book_name}")
async def delete_book(book_name:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('name').casefold()== book_name.casefold():
            BOOKS.pop(i)
            break