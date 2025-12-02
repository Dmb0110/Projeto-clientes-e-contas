# API de clientes e contas

## Descrição
API desenvolvida em **FastAPI** para gerenciar clientes e suas contas.  
Permite cadastrar um cliente e varias contas no nome dele

Permite cadastrar e consultar motos informando **marca** e **modelo**.

------------------------------------------------------

## ⚙️ Tecnologias utilizadas
- **Python 3.13.0** → linguagem principal do projeto
- **FastAPI** → framework web moderno e assíncrono
- **SQLAlchemy** → ORM para manipulação do banco de dados
- **Alembic** → ferramenta de migração de banco de dados
- **PostgreSQL (Neon)** → banco de dados relacional utilizado
- **Autenticação: JWT** → controle de acesso com tokens
- **Servidor: Uvicorn** → servidor ASGI para rodar a aplicação
- **Ferramentas de testes: Pytest** → testes automatizados

------------------------------------------------------

## Instalação e execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/Dmb0110/Projeto-clientes-e-contas.git
   cd teste12

------------------------------------------------------
## (Visão geral do projeto)
Título: Nome claro do projeto (ex.: “projeto clientes e contas”).

Descrição: Permite adicionar varios clientes e varias contas para cada cliente

Principais recursos: Um cliente cadastrado pode ter varias contas em seu nome.

Tecnologias: Python, FastAPI, SQLAlchemy, Alembic, PostgreSQL (Neon).

------------------------------------------------------
## (Pré-requisitos)
Versões: Python 3.13.0, PostgreSQL 17.

Dependências: FastAPI, Uvicorn, SQLAlchemy, Alembic, psycopg2.

Acesso ao banco: String de conexão válida (ex.: Neon com sslmode).

------------------------------------------------------
## [CONFIGURAÇAO E INSTALAÇAO]
## (Clonar o repositório):

git clone https://github.com/Dmb0110/Projeto-clientes-e-contas.git

cd teste12

-----------------------------------------------------
## (Criar/ativar ambiente virtual):

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

-----------------------------------------------------
## (Instalar dependências):


pip install -r requirements.txt

-----------------------------------------------------
## (Variáveis de ambiente (.env)):

DATABASE_URL=postgresql+psycopg2://usuario:senha@host:5432/nome_do_banco?sslmode=require


-----------------------------------------------------
## (Configurar Alembic (se aplicável)):

Verifique alembic.ini e alembic/env.py apontando para DATABASE_URL.

-----------------------------------------------------
## (Migrações e execução)
Aplicar migrações:

alembic upgrade head
Rodar servidor:

uvicorn app.main:app --reload

-----------------------------------------------------
## (URLs de documentação):

Swagger: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

-----------------------------------------------------
## {Endpoints da API}

## [Rotas públicas do cliente]

## Criar cliente (POST /cliente):

Body da requisiçao:

json
{
  "nome": "anônimo",
  "idade": "36"
}

Resposta da requisiçao:

json
{
  "id": 1,
  "nome": "anônimo1",
  "idade": "36"
}

-----------------------------------------------------
## Listar clientes (GET /cliente):

Resposta:

json
[
  { "id": 1, "nome": "anônimo1", "idade": "36" },
  { "id": 2, "nome": "anônimo2", "idade": "25" }
]

-----------------------------------------------------
## Buscar clientes por id (GET /cliente/{id})

json
{
  "id": 1,
  "nome": "anônimo1",
  "idade": "36"
}

-----------------------------------------------------
## Atualizar cliente (PUT /cliente/{id})

Body da requisiçao:

json
{
  "nome": "anônimo atualizado",
  "idade": "40"
}

Body da resposta:

json
{
  "id": 1,
  "nome": "anônimo atualizado",
  "idade": "40"
}


-----------------------------------------------------
## Deletar cliente (DELETE /cliente/{id})

Resposta:
{
  "message": "Cliente deletado com sucesso"
}


-----------------------------------------------------
## [Rotas públicas de conta]

## Criar conta (POST /conta)

Body da requisiçao:

json
{
  "nome do banco ": "banco xyz",
  "numero da agencia": "0102",
  "numero da conta":"123456",
  "cliente_id":"1"
}

Resposta da requisiçao:

json
{
  "id": 1,
  "nome do banco ": "banco xyz",
  "numero da agencia": "0102",
  "numero da conta":"123456",
  "cliente_id":"1"
}

-----------------------------------------------------

## Listar contas (GET /conta):

Resposta:

json
[
  {
    "id": 1,
    "nome do banco ": "banco xyz",
    "numero da agencia": "0102",
    "numero da conta":"10",
    "cliente_id":"1"
  }

  {
    "id": 2,
    "nome do banco ": "banco xyz",
    "numero da agencia": "0103",
    "numero da conta":"11",
    "cliente_id":"2"
  }
]

-----------------------------------------------------
## Atualizar conta (PUT /conta/{id})

Body da requisiçao:

{
    "id": 2,
    "nome do banco ": "banco xyz",
    "numero da agencia": "0103",
    "numero da conta":"11",
    "cliente_id":"2"
}

Body da resposta:

{
    "id": 2,
    "nome do banco ": "banco xyz atualizado",
    "numero da agencia": "0103",
    "numero da conta":"11",
    "cliente_id":"2"
}

-----------------------------------------------------
## Deletar conta (DELETE /conta/{id})

Resposta:
{
  "message": "Conta deletada com sucesso"
}


-----------------------------------------------------
-----------------------------------------------------
## [Rotas privadas do cliente]

## Criar cliente (POST /cliente)
Cria um novo cliente no sistema.

**Body da requisição***:
json
{
  "nome": "anônimo",
  "idade": "20"
}

Body da Resposta:

json
{
  "id": 1,
  "nome": "anônimo",
  "idade": "20"
}

-----------------------------------------------------
## Listar cliente (GET /cliente)
Retorna todas os clientes cadastrados.

Resposta:

json
[
  { "id": 1, "nome": "anônimo1", "idade": "60" },
  { "id": 2, "nome": "anônimo2", "idade": "25" }
]

-----------------------------------------------------
## [Rotas privadas de conta]

## Criar conta (POST /conta)

Body da requisiçao:

json
{
  "nome do banco ": "banco xyz",
  "numero da agencia": "0102",
  "numero da conta":"123456",
  "cliente_id":"2"
}

Body da Resposta:

json
{
  "id": 1,
  "nome do banco ": "banco xyz",
  "numero da agencia": "0102",
  "numero da conta":"123456",
  "cliente_id":"2"
}

-----------------------------------------------------

## Listar contas (GET /contas):

Resposta:

json
[
  {
    "id": 1,
    "nome do banco ": "banco xyz",
    "numero da agencia": "0102",
    "numero da conta":"10",
    "cliente_id":"2"
  }

  {
    "id": 2,
    "nome do banco ": "banco xyz",
    "numero da agencia": "0103",
    "numero da conta":"11",
    "cliente_id":"2"
  }
]

-----------------------------------------------------
## 🔐 Autenticação com JWT

Este projeto utiliza **JSON Web Tokens (JWT)** para autenticação e autorização.  
Usuários devem se registrar e fazer login para obter um token de acesso.  
Esse token deve ser enviado no cabeçalho das requisições para acessar endpoints protegidos.

### Fluxo de autenticação
1. **Registro de usuário**  
  ## (POST /registro)  
   Body:
   ```json
   {
     "username": "anônimo",
     "password": "senha123"
   }


## Login (POST /login)
Autentica o usuário e retorna um token JWT.

Body da requisição:

json
{
  "username": "joao",
  "password": "senha123"
}

Resposta da requisiçao:

{
  "access_token": "jwt_token_aqui",
  "token_type": "bearer"
}

-----------------------------------------------------
## (Modelo de dados e validação)
**Entidade Cliente: campos mínimos**

id: inteiro autoincremento.
nome: string obrigatória.
idade: string obrigatória.

Regras básicas:

nome/idade não vazios: validar no schema (Pydantic).

Erros comuns: retornar 422 para payload inválido.


**Entidade Conta**

id: inteiro autoincremento
nome do banco:string obrigatória
numero da agencia: inteiro obrigatória
numero da conta: inteiro obrigatório
cliente id: nâo e obrigatorio

Regras basicas:

nome do banco/numero da agencia/numero da conta não vazios: validar no schema(Pydantic)

Erros comuns: retornar 422 para payload inválida


**Entidade User**

id: inteiro autoincremento
username: string obrigatoria,único (não pode repetir)
password: string obrigatoria,armazenada com hash (não em texto puro)

Validações:

Username não pode ser vazio e deve ser único
Password deve ser validado e armazenado com hashing seguro (ex: **bcrypt** viar Passlib) 
Retornar 422 em caso de payload inválido


## Autenticação
- Usuários devem se registrar e fazer login para obter um **JWT token**  
- O token deve ser enviado no cabeçalho: 

-------------------------------------------------------
## (Testes e qualidade)
Rodar testes:

pytest

-------------------------------------------------------
## (Deploy (opcional))
Container: Dockerfile e docker-compose para app + banco.

Variáveis de produção: DATABASE_URL segura

Health check: endpoint simples (ex.: GET /health retornando 200).

------------------------------------------------------
## 📂 Estrutura do projeto
app/
 ├── main.py
 ├── auth/jwt.py
 ├── core/config.py        
 ├── crud_services/       # 6 arquivos
 ├── database/session.py
 ├── models/              # 2 arquivos
 ├── models_usuario/usuario.py
 ├── routers2/            # 6 arquivos
 ├── routers.py
 ├── schemas/           # 2 arquivos

alembic/                   # migrações
requirements.txt           # dependências
README.md                  # documentação

