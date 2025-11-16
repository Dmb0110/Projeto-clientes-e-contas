from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.conta_schema import CriarConta, ContaOut
from app.database.session import get_db
from app.auth.jwt import verificar_token
from app.crud_services.conta_auth_service import ContaService

router = APIRouter()

@router.post(
    "/",
    summary="Rota protegida para criar conta",
    response_model=ContaOut,
    status_code=status.HTTP_201_CREATED
)
def criar_conta(
    criar: CriarConta,
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)  # exige autenticação via JWT
):
    """
    Cria uma nova conta.
    - `criar`: dados validados pelo schema CriarConta.
    - `db`: sessão do banco injetada via Depends.
    - `usuario`: resultado da verificação do token JWT.
    Retorna a conta criada como ContaOut.
    """
    return ContaService.criar_conta_auth(criar, db)

@router.get(
    "/",
    summary="Rota protegida que retorna todas as contas",
    response_model=list[ContaOut],
    status_code=status.HTTP_200_OK
)
def listar_contas(
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)  # exige autenticação via JWT
):
    """
    Lista todas as contas cadastradas.
    - `db`: sessão do banco injetada via Depends.
    - `usuario`: resultado da verificação do token JWT.
    Retorna uma lista de ContaOut.
    """
    return ContaService.listar_contas_auth(db)
