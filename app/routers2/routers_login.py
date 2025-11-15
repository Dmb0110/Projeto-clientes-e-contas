from fastapi import APIRouter,Depends
from app.schemas.cliente_schema import LoginUsuario
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.crud_services.login_service import LoginService

router = APIRouter()
# Endpoitn para login e geração de token
@router.post(
    "/login",
    summary='Cria login para o usuario e gerar o token',
    status_code=201
)
async def login(request: LoginUsuario,db: Session = Depends(get_db)):
    return LoginService.login(request,db)

