from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

app = FastAPI()

BOOKS = [
    {"name": "venkat", "age": "22", "address": "snk"},
    {"name": "raman", "age": "23", "address": "mrkp"},
    {"name": "raju", "age": "22", "address": "drnk"},
]

@app.get("/books")
async def read_books():
    return BOOKS

@app.get("/books/{dynamicparm}")
async def read_book(dynamicparm: str):
    for book in BOOKS:
        if book.get("name").casefold() == dynamicparm.casefold():
            return book
    return {"error": "Book not found"}

@app.get("/books/")
async def read_books_by_query(age: str):
    books_filtered = [book for book in BOOKS if book.get("age").casefold() == age.casefold()]
    return books_filtered

@app.post("/books/create_book")
async def create_book(new_book: dict):
    BOOKS.append(new_book)
    return {"message": "Book added successfully", "book": new_book}

# This part allows the FastAPI app to run using http.server
if __name__ == "__main__":
    import threading

    def run_app():
        import fastapi
        import os
        from fastapi import FastAPI
        from fastapi.middleware.wsgi import WSGIMiddleware
        from werkzeug.serving import run_simple

        # Wrap the FastAPI app using WSGI interface
        app = FastAPI()

        # Serve the FastAPI app using Python's HTTP server
        run_simple('127.0.0.1', 8080, app)
