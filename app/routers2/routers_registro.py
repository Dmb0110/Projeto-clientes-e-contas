from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.cliente_schema import CriarUsuario
from app.database.session import get_db
from app.crud_services.registro_service import RegistroService

router = APIRouter()

# Endpoint para registrar novo usuário
@router.post(
    "/",
    summary="Registrar novo usuário",
    status_code=201
)
async def registrar_usuario(
    request: CriarUsuario,
    db: Session = Depends(get_db)
):
    """
    Rota de registro de usuário:
    - Recebe dados validados pelo schema CriarUsuario (username e password).
    - Usa a sessão do banco (db) injetada via Depends.
    - Chama RegistroService.registrar_usuario para verificar duplicidade,
      criptografar senha e salvar no banco.
    Retorna mensagem de sucesso ou lança HTTPException em caso de erro.
    """
    return RegistroService.registrar_usuario(request, db)
