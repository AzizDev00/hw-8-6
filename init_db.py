from database import Base, engine
from models import Book, User, Review, Author, BookCategory, BookAuthor

Base.metadata.create_all(bind=engine)