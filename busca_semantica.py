import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# Dados de teste para simular o banco de conhecimento
DOCUMENTOS_MOCK = [
    "FastAPI é um framework web moderno e rápido para construir APIs com Python.",
    "O Django é um framework completo focado em desenvolvimento rápido e design limpo.",
    "RAG (Retrieval-Augmented Generation) ajuda LLMs a consultarem dados externos para evitar alucinações."
]

def rodar_busca_semantica():
    # Converte textos para instâncias de Document
    docs = [Document(page_content=texto) for texto in DOCUMENTOS_MOCK]
    
    # Modelo de Embeddings da OpenAI
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    # Ingestão e criação do indexador do banco vetorial local FAISS
    banco_vetorial = FAISS.from_documents(docs, embeddings)
    
    query = "Quero uma ferramenta Python para construir rotas de internet"
    print(f"Buscando semanticamente por: '{query}'\n")
    
    # Busca pelo documento mais relevante (k=1)
    resultados = banco_vetorial.similarity_search(query, k=1)
    print(f"Resultado mais próximo encontrado:\n-> {resultados[0].page_content}")

if __name__ == "__main__":
    try:
        rodar_busca_semantica()
    except Exception as e:
        print("[Aviso]: Para rodar este script, certifique-se de configurar sua OPENAI_API_KEY no terminal.")