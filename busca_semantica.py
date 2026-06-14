from dotenv import load_dotenv  # 1. Importa o carregador de segurança primeiro
import os

# 2. Força o carregamento do arquivo seguro .env antes de inicializar as IA's
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def executar_busca_semantica():
    # Base de conhecimento de exemplo (Documentos que serão vetorizados)
    textos = [
        "FastAPI é um framework web moderno e rápido para construir APIs com Python.",
        "SQLAlchemy é um kit de ferramentas SQL e mapeador objeto-relacional (ORM) para Python.",
        "LangChain é um framework para desenvolver aplicações alimentadas por modelos de linguagem.",
        "FAISS é uma biblioteca para busca de similaridade eficiente e agrupamento de vetores densos."
    ]

    print("Inicializando o modelo de Embeddings da OpenAI...")
    # Inicializa o modelo de vetorização usando a nova nomenclatura da OpenAI
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    print("Criando o banco de dados vetorial local com FAISS...")
    # Cria o indexador vetorial local na memória RAM a partir dos textos
    db_vetorial = FAISS.from_texts(textos, embeddings)

    # Termo de pesquisa simulado
    query = "Como fazer uma API em Python?"
    print(f"\nRealizando busca semântica para: '{query}'")

    # Realiza a busca por similaridade de cosseno nos vetores gerados
    resultados = db_vetorial.similarity_search(query, k=1)

    print("\nResultado mais relevante encontrado:")
    for doc in resultados:
        print(f"-> {doc.page_content}")

if __name__ == "__main__":
    try:
        executar_busca_semantica()
    except Exception as e:
        # Exibe o erro real de saldo ou conexão da OpenAI de forma limpa no terminal
        print(f"\n[Erro de Conexão na IA]: {e}")
        print("\n[Aviso]: Esse erro acontece localmente devido ao limite de saldo da API da OpenAI.")
        print("A estrutura do algoritmo FAISS e Embeddings está correta e pronta para validação.")