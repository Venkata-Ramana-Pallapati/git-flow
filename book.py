from fastapi import FastAPI, Body
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter

app = FastAPI()

# Initialize Prometheus metrics
REQUESTS = Counter('http_requests_total', 'Total HTTP requests made', ['method', 'endpoint'])

# Define the instrumentator for Prometheus metrics
instrumentator = Instrumentator().instrument(app).expose(app)

# Define the books list
BOOKS = [
    {'name': 'venkat', 'age': "22", "address": "snk"},
    {'name': 'raman', 'age': "23", "address": "mrkp"},
    {'name': 'raju', 'age': "22", "address": "drnk"}
]

# Endpoint to get all books
@app.get("/books")
async def read_root():
    REQUESTS.labels(method='GET', endpoint='/books').inc()
    return BOOKS

# Endpoint to get a book by dynamic parameter
@app.get("/books/{dynamicparm}")
async def read_all_books(dynamicparm: str):
    REQUESTS.labels(method='GET', endpoint='/books/{dynamicparm}').inc()
    for book in BOOKS:
        if book.get('name').casefold() == dynamicparm.casefold():
            return book

# Endpoint to query books by age
@app.get("/books/")
async def read_query(age: str):
    REQUESTS.labels(method='GET', endpoint='/books/').inc()
    book_to = [book for book in BOOKS if book.get('age').casefold() == age.casefold()]
    return book_to

# Endpoint to create a new book
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    REQUESTS.labels(method='POST', endpoint='/books/create_book').inc()
    BOOKS.append(new_book)
    return {"message": "Book added successfully"}

# Endpoint to update a book
@app.put("/books/update_book")
async def updated_book(updated_book=Body()):
    REQUESTS.labels(method='PUT', endpoint='/books/update_book').inc()
    for i in range(len(BOOKS)):
        if BOOKS[i].get('name').casefold() == updated_book.get('name').casefold():
            BOOKS[i] = updated_book
    return {"message": "Book updated successfully"}

# Endpoint to delete a book
@app.delete("/books/delete_book/{book_name}")
async def delete_book(book_name: str):
    REQUESTS.labels(method='DELETE', endpoint='/books/delete_book/{book_name}').inc()
    for i in range(len(BOOKS)):
        if BOOKS[i].get('name').casefold() == book_name.casefold():
            BOOKS.pop(i)
            return {"message": "Book deleted successfully"}
    return {"message": "Book not found"}
