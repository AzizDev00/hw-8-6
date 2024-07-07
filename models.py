from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(Text)
    reviews = relationship("Review", back_populates="user")
    
    def __repr__(self):
        return f"<User {self.username}>"
    

class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    year = Column(Integer)
    book_authors = relationship("BookAuthor", back_populates="author")

    def __repr__(self):
        return f"<Author {self.name} {self.surname}>"
    

class BookCategory(Base):
    __tablename__ = "book_category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    books = relationship("Book", back_populates="category")

    def __repr__(self):
        return f"<Category {self.name}>"

class BookAuthor(Base):
    __tablename__ = "book_author"
    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey('author.id'))
    book_id = Column(Integer, ForeignKey('book.id'))
    author = relationship("Author", back_populates="book_authors")
    book = relationship("Book", back_populates="authors")

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    ISBN = Column(String, unique=True, index=True)
    price = Column(Integer)
    image = Column(Text)
    year = Column(Integer)
    category_id = Column(Integer, ForeignKey('book_category.id'))
    category = relationship("BookCategory", back_populates="books")
    reviews = relationship("Review", back_populates="book")
    authors = relationship("BookAuthor", back_populates="book")

    def __repr__(self):
        return f"<Book {self.name}>"
    
class Review(Base):
    __tablename__ = "review"
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(Text)
    star_given = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    book_id = Column(Integer, ForeignKey('book.id'))
    user = relationship("User", back_populates="reviews")
    book = relationship("Book", back_populates="reviews")

    def __repr__(self):
        return f"<Review {self.star_given} stars>"
