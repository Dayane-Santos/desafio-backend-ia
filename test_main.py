import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from database import Base, BookModel
from main import app, get_db

# 1. Configura o banco em memória usando o StaticPool para compartilhar a mesma conexão
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # ESSA LINHA RESOLVE O PROBLEMA DE COMPARTILHAMENTO
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. Força a criação das tabelas no pool estático de memória
Base.metadata.create_all(bind=engine)

# 3. Substitui a sessão de banco original da API pela sessão de testes com escopo correto
def override_get_db():
    database = TestingSessionLocal()
    try:
        yield database
    finally:
        database.close()

app.dependency_overrides[get_db] = override_get_db

# 4. Inicializa o cliente de testes
client = TestClient(app)

@pytest.fixture(autouse=True)
def clean_db():
    """Garante que a tabela seja limpa antes de cada teste"""
    session = TestingSessionLocal()
    try:
        session.query(BookModel).delete()
        session.commit()
    finally:
        session.close()
    yield

# --- Seus testes unitários ---

def test_create_book():
    """Testa se o cadastro de livros funciona com sucesso"""
    payload = {
        "title": "O Hobbit", 
        "author": "Tolkien", 
        "published_date": "1937-09-21", 
        "summary": "Uma grande jornada de aventura."
    }
    response = client.post("/books", json=payload)
    assert response.status_code == 201
    
    data = response.json()
    assert data["title"] == "O Hobbit"
    assert "id" in data

def test_get_books_filter():
    """Testa se a consulta e a filtragem parcial por título funcionam"""
    # Cadastra previamente um livro de teste
    client.post("/books", json={
        "title": "Python Avancado", 
        "author": "Guido van Rossum", 
        "published_date": "2020-01-01", 
        "summary": "Estudo aprofundado de Python."
    })
    
    # Realiza a busca enviando apenas parte do termo 'Python'
    response = client.get("/books?title=Python")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 1
    assert data[0]["author"] == "Guido van Rossum"