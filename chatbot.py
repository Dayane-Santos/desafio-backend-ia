from dotenv import load_dotenv # Importa o carregador primeiro
import os

# 1. Força o carregamento do arquivo .env ANTES de qualquer outra biblioteca
load_dotenv()

# 2. Agora sim importamos o restante do ecossistema LangChain e OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def criar_chatbot_python():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente especialista em programação Python. Responda com clareza e didática."),
        ("user", "{pergunta}")
    ])

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    output_parser = StrOutputParser()

    return prompt | llm | output_parser

if __name__ == "__main__":
    bot = criar_chatbot_python()
    pergunta_exemplo = "Como criar uma lista em Python?"
    print(f"Usuário perguntou: {pergunta_exemplo}\n")
    
    try:
        resposta = bot.invoke({"pergunta": pergunta_exemplo})
        print(f"Resposta do Chatbot:\n{resposta}")
    except Exception as e:
        # Agora o terminal vai nos mostrar o erro real que a OpenAI devolveu
        print(f"[Erro de Conexão]: {e}\n")
        print("[Aviso]: Se o erro acima for de credenciais, verifique se o arquivo .env foi salvo na pasta correta.")