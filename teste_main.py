import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import database as db
from main import app, get_db

# Cria um banco de dados temporário em memória exclusivo para testes
engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        session = TestingSessionLocal()
        yield session
    finally:
        session.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    db.Base.metadata.create_all(bind=engine)
    yield
    db.Base.metadata.drop_all(bind=engine)

def test_create_book():
    payload = {"title": "O Hobbit", "author": "Tolkien", "published_date": "1937", "summary": "Uma grande jornada"}
    response = client.post("/books", json=payload)
    assert response.status_code == 201

def test_get_books_filter():
    client.post("/books", json={"title": "Python Avançado", "author": "Guido", "published_date": "2020", "summary": "Estudo de Python"})
    response = client.get("/books?title=Python")
    assert response.status_code == 200
    assert len(response.json()) == 1