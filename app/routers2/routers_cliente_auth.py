from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from app.schemas.cliente_schema import CriarCliente, ClienteOut
from app.database.session import get_db
from app.auth.jwt import verificar_token
from app.crud_services.cliente_auth_service import ClienteService

router = APIRouter()

# Middleware de segurança baseado em token Bearer (JWT)
security = HTTPBearer()

@router.post(
    "/",
    summary="Rota protegida para criar cliente",
    response_model=ClienteOut,
    status_code=status.HTTP_201_CREATED
)
def criar_cliente(
    criar: CriarCliente,
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)  # garante que apenas usuários autenticados acessem
):
    """
    Cria um novo cliente.
    - `criar`: dados validados pelo schema CriarCliente.
    - `db`: sessão do banco injetada via Depends.
    - `usuario`: resultado da verificação do token JWT.
    Retorna o cliente criado como ClienteOut.
    """
    return ClienteService.criar_cliente_auth(criar, db)

@router.get(
    "/",
    summary="Rota protegida que retorna todos os clientes",
    response_model=list[ClienteOut],
    status_code=status.HTTP_200_OK
)
def listar_clientes(
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)  # exige autenticação
):
    """
    Lista todos os clientes cadastrados.
    - `db`: sessão do banco injetada via Depends.
    - `usuario`: resultado da verificação do token JWT.
    Retorna uma lista de ClienteOut.
    """
    return ClienteService.listar_clientes_auth(db)
