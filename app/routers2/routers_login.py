from fastapi import APIRouter, Depends
from app.schemas.cliente_schema import LoginUsuario
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.crud_services.login_service import LoginService

router = APIRouter()

# Endpoint para login e geração de token JWT
@router.post(
    "/",
    summary="Cria login para o usuário e gera o token",
    status_code=201
)
async def login(request: LoginUsuario, db: Session = Depends(get_db)):
    """
    Rota de autenticação:
    - Recebe credenciais do usuário (username e password) via schema LoginUsuario.
    - Usa a sessão do banco (db) injetada via Depends.
    - Chama LoginService.login para validar credenciais e gerar token JWT.
    Retorna um dicionário com o access_token.
    """
    return LoginService.login(request, db)
