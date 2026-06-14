from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
import database as db
import schemas

app = FastAPI(title="API de Biblioteca Virtual")

# Inicializa o banco de dados quando a API liga
@app.on_event("startup")
def on_startup():
    db.init_db()

# Abre e fecha as conexões com o banco de forma segura
def get_db():
    database = db.SessionLocal()
    try:
        yield database
    finally:
        database.close()

# Rota para cadastrar livros
@app.post("/books", response_model=schemas.BookResponse, status_code=201)
def create_book(book: schemas.BookCreate, session: Session = Depends(get_db)):
    db_book = db.BookModel(
        title=book.title,
        author=book.author,
        published_date=book.published_date,
        summary=book.summary
    )
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

# Rota para consultar livros com filtros parciais opcionais
@app.get("/books", response_model=List[schemas.BookResponse])
def get_books(
    title: Optional[str] = Query(None),
    author: Optional[str] = Query(None),
    session: Session = Depends(get_db)
):
    query = session.query(db.BookModel)
    if title:
        query = query.filter(db.BookModel.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(db.BookModel.author.ilike(f"%{author}%"))
    return query.all()