from pydantic import BaseModel

# Formato exigido para cadastrar um livro (Validação de Entrada)
class BookCreate(BaseModel):
    title: str
    author: str
    published_date: str
    summary: str

# Formato que a API devolve (Inclui o ID automático do banco)
class BookResponse(BookCreate):
    id: int

    class Config:
        from_attributes = True