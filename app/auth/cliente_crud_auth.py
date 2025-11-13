

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.models.cliente_model import Cliente
from app.schemas.cliente_schema import CriarCliente, ClienteOut
from app.database.session import get_db
from app.auth.jwt import verificar_token

router = APIRouter()

@router.post(
    "/",
    summary="Rota protagida Criar cliente",
    response_model=ClienteOut
)
def criar_cliente(
    criar: CriarCliente,
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):
    novo_cliente = Cliente(**criar.dict())
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente
'''
@router.get(
    '/',
    summary='Rota protegida quer retorna todos os usuarios',
    response_model=ClienteOut
)
def receber(
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):
    return db.query(Cliente).all()
'''


@router.get(
    "/",
    summary='Rota protegida quer retorna todos os usuarios',
    response_model=list[ClienteOut]
)
def listar_clientes(
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):
    clientes = db.query(Cliente).all()
    return [ClienteOut.model_validate(cliente) for cliente in clientes]


