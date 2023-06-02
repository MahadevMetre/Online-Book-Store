from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define Book model
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    cover_image: str
    price: float
    rating: float

# In-memory database
books_db = [
    Book(
        id=1,
        title="Book 1",
        author="Author 1",
        description="Description 1",
        cover_image="image1.jpg",
        price=9.99,
        rating=4.5
    ),
    Book(
        id=2,
        title="Book 2",
        author="Author 2",
        description="Description 2",
        cover_image="image2.jpg",
        price=14.99,
        rating=3.9
    ),
    # Add more books as needed
]

# Route to get all books
@app.get('/books', response_model=List[Book])
def get_books():
    return books_db

# Route to search books by title, author, or category
@app.get('/books/search', response_model=List[Book])
def search_books(query: str):
    filtered_books = [
        book for book in books_db
        if query.lower() in book.title.lower() or query.lower() in book.author.lower()
    ]
    return filtered_books
