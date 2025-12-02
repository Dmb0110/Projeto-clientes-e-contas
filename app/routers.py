from fastapi import APIRouter
from app.routers2.routers_crud_cliente import router as cliente
from app.routers2.routers_crud_conta import router as conta
from app.routers2.routers_cliente_auth import router as cliente_auth
from app.routers2.routers_conta_auth import router as conta_auth
from app.routers2.routers_registro import router as registro
from app.routers2.routers_login import router as login

# Cria um roteador principal para agrupar todos os sub-routers
api_router = APIRouter()

# Rotas públicas de autenticação/registro
api_router.include_router(registro, prefix="/registro", tags=["registro"])
api_router.include_router(login, prefix="/login", tags=["login"])

# Rotas protegidas (com JWT) para cliente e conta
api_router.include_router(cliente_auth, prefix="/cliente_auth", tags=["cliente_auth"])
api_router.include_router(conta_auth, prefix="/conta_auth", tags=["conta_auth"])

# Rotas públicas para cliente e conta
api_router.include_router(cliente, prefix="/cliente", tags=["cliente"])
api_router.include_router(conta, prefix="/conta", tags=["conta"])
