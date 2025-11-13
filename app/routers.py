from fastapi import APIRouter
from app.routers2.routers_cliente import router as cliente
from app.routers2.routers_conta import router as conta
#from app.crud_services.conta_service import router as conta
from app.auth.cliente_crud_auth import router as cliente_auth
from app.auth.conta_crud_auth import router as conta_auth
from app.auth.jwt import router

api_router = APIRouter()
api_router.include_router(router)
api_router.include_router(cliente_auth,prefix='/cliente_auth',tags=['cliente_auth'])
api_router.include_router(conta_auth,prefix='/conta_auth',tags=['conta_auth'])
api_router.include_router(cliente,prefix='/cliente',tags=['cliente'])
api_router.include_router(conta,prefix='/conta',tags=['conta'])
