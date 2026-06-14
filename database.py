from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Indica onde o arquivo do banco de dados vai ser criado no seu computador
SQLALCHEMY_DATABASE_URL = "sqlite:///./biblioteca.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo do Banco de Dados para a tabela de Livros
class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    published_date = Column(String, nullable=False)
    summary = Column(Text, nullable=False)

# Função para ligar o banco de dados e criar as tabelas
def init_db():
    Base.metadata.create_all(bind=engine)