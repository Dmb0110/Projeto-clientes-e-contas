from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.models.conta_model import Conta
from app.schemas.conta_schema import CriarConta, ContaOut
from app.database.session import get_db
from app.auth.jwt import verificar_token

router = APIRouter()

@router.post(
    "/",
    summary="Rota protegida Criar conta",
    response_model=ContaOut
)
def criar_conta(
    criar: CriarConta,
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):
    nova_conta = Conta(**criar.dict())
    db.add(nova_conta)
    db.commit()
    db.refresh(nova_conta)
    return nova_conta

'''
@router.get(
    '/',
    summary='Rota protegida que retorna todos as contas',
    response_model=ContaOut
)
def receber(
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):
    return db.query(Conta).all()

'''


@router.get(
    "/",
    summary='Rota protegida que retorna todos as contas',
    response_model=list[ContaOut]
)
def listar_clientes(
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):
    clientes = db.query(Conta).all()
    return [ContaOut.model_validate(cliente) for cliente in clientes]


