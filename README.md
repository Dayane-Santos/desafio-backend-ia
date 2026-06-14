# desafio-backend-ia
# 🚀 Desafio Técnico – Desenvolvimento de API & Engenharia de IA

Este repositório contém a solução completa para o teste técnico de desenvolvedor backend focado em Inteligência Artificial. O projeto foi construído utilizando as melhores e mais modernas práticas de mercado para arquitetura de software em Python, validação rígida de tipos e orquestração de Large Language Models (LLMs).

---

## 🛠️ Stack Técnica e Frameworks

A arquitetura do projeto foi desenhada para isolar responsabilidades e garantir máxima performance:
- **Core Web (Questão 1):** FastAPI (utilizando recursos nativos de injeção de dependência e tipagem do Python).
- **Persistência Tradicional (Questão 1):** SQLAlchemy ORM mapeando dados de forma limpa em um banco de dados estruturado local `SQLite`.
- **Suite de Testes (Questão 1):** Pytest integrado com o `HTTPX (TestClient)` para simulação de requisições de forma isolada.
- **Orquestração de IA (Questão 2):** LangChain utilizando a sintaxe contemporânea declarativa **LCEL (LangChain Expression Language)** e modelo `gpt-4o-mini` da OpenAI.
- **Vetorização e RAG (Questão 3):** OpenAI Embeddings (`text-embedding-3-small`) integrado à biblioteca `FAISS` (Facebook AI Similarity Search) para indexação vetorial local de alta velocidade.

---

## 📂 Estrutura de Diretórios do Projeto

```text
DESAFIO_BACKEND_IA/
├── database.py         # Configuração do Engine, Session do SQLAlchemy e Modelos Relacionais
├── schemas.py          # Camada de validação de dados e DTOs estruturados via Pydantic
├── main.py             # Inicialização do FastAPI, gerenciamento de rotas HTTP e injeção de dependências
├── test_main.py        # Suite de testes unitários automatizados com isolamento de banco em memória
├── chatbot.py          # Módulo isolado de IA Generativa especializado em Python via LangChain
├── busca_semantica.py   # Pipeline completo de ingestão, vetorização e busca semântica em banco vetorial
└── requirements.txt    # Gerenciador de dependências e pacotes do projeto

🏃‍♂️ Como Executar e Homologar o Projeto
Siga os passos abaixo sequencialmente no terminal do seu editor de código para validar todas as entregas locais do desafio.

1. Isolamento do Ambiente Virtual (Virtualenv)
Crie e ative a bolha do ambiente virtual isolado para garantir que os pacotes não interfiram globalmente no seu sistema operacional:

# Criar o ambiente virtual
python -m venv venv

# Ativar no Windows (Prompt de Comando - CMD)
venv\Scripts\activate

# Ativar no Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Ativar no Linux / macOS
source venv/bin/activate

(Certifique-se de que o prefixo (venv) apareça no início da linha do terminal antes de continuar).

2. Instalação de Dependências
Realize a instalação em lote de todas as bibliotecas necessárias declaradas no escopo técnico:

pip install -r requirements.txt

3. Validação da Suite de Testes (Questão 1)
Antes de subir o servidor, garanta a estabilidade e a qualidade das regras de negócio executando os testes automatizados criados em ambiente efêmero de memória:

pytest

4. Inicializando e Testando a API de Livros (Questão 1)
Para subir o servidor HTTP local na porta padrão 8000, execute o servidor ASGI Uvicorn:

uvicorn main:app --reload

Abra o navegador da sua escolha e acesse a documentação interativa autogerada pelo framework:
👉 Acesse em: http://127.0.0.1:8000/docs

Através do Swagger UI, você poderá realizar simulações de disparos reais de POST para alimentar o banco de dados e filtros parciais dinâmicos de GET para buscar por fragmentos de títulos ou nomes de autores.

🛑 Importante para as Questões 2 e 3: Os módulos seguintes realizam integrações com a API oficial da OpenAI. Antes de rodá-los, encerre o servidor uvicorn apertando Ctrl + C e configure sua chave de acesso contendo créditos ativos no seu terminal:

No Windows CMD: set OPENAI_API_KEY=sk-sua-chave-aqui

No Windows PowerShell: $env:OPENAI_API_KEY="sk-sua-chave-aqui"

No Linux / macOS: export OPENAI_API_KEY="sk-sua-chave-aqui"

5. Executando o Chatbot de Engenharia de IA (Questão 2)
Dispare o script modular para interagir com a cadeia inteligente que responde dúvidas focadas e restritas ao escopo da linguagem Python:

python chatbot.py

6. Executando o Mecanismo de Busca Semântica (Questão 3)
Inicie o pipeline de geração de Embeddings que demonstra o conceito de vetorização inteligente para recuperação de informações (RAG Core) utilizando o FAISS local:

python busca_semantica.py

🚀 Desenvolvido com foco em boas práticas de engenharia de software e inteligência artificial aplicada.