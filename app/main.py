from fastapi import FastAPI
from app.database.session import Base, engine
from app.routers import api_router

# Instância principal da aplicação FastAPI
app = FastAPI(
    title="API de Clientes e Contas",
    description="Gerencia clientes e suas contas bancárias",
    version="1.0.0",
    docs_url="/docs",   # URL para Swagger UI
    redoc_url="/redoc"  # URL para ReDoc
)

# Cria todas as tabelas definidas nos modelos ORM (Cliente, Conta, Usuario, etc.)
Base.metadata.create_all(bind=engine)

# Inclui o roteador principal que agrega todas as rotas da aplicação
app.include_router(api_router)

'''
Um dev pleno normalmente acrescentaria:

Autenticação/autorização (JWT, OAuth2).

Testes mais robustos (fixtures, banco em memória, mocks).

CI/CD configurado (pipeline automático de testes e deploy).

Documentação mais completa (README com instruções de setup, exemplos de uso da API).

Camadas de serviço para separar lógica de negócio do acesso ao banco.



cliente_conta_api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── cliente_model.py
│   │   └── conta_model.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── cliente_schema.py
│   │   └── conta_schema.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── cliente_crud.py
│   │   └── conta_crud.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── cliente_routes.py
│   │   └── conta_routes.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── connection.py
│   └── core/
│       ├── __init__.py
│       └── config.py
├── .env
├── requirements.txt
└── README.md

'''

