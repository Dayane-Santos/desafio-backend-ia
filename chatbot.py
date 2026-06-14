import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def criar_chatbot_python():
    # Define o prompt do sistema instruindo o comportamento do especialista
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente especialista em programação Python. Responda com clareza e didática."),
        ("user", "{pergunta}")
    ])

    # Utiliza o modelo gpt-4o-mini
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    output_parser = StrOutputParser()

    # Criação do fluxo com a sintaxe moderna LCEL
    return prompt | llm | output_parser

if __name__ == "__main__":
    bot = criar_chatbot_python()
    pergunta_exemplo = "Como criar uma lista em Python?"
    print(f"Usuário perguntou: {pergunta_exemplo}\n")
    
    try:
        resposta = bot.invoke({"pergunta": pergunta_exemplo})
        print(f"Resposta do Chatbot:\n{resposta}")
    except Exception as e:
        print("[Aviso]: Para rodar este script, certifique-se de configurar sua OPENAI_API_KEY no terminal.")