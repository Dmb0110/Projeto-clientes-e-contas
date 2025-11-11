from fastapi import status,APIRouter,HTTPException,Depends,FastAPI
from sqlalchemy.orm import Session
from app.models.cliente_model import Cliente
from app.schemas.cliente_schema import CriarCliente,ClienteOut,AtualizarCliente,DeletarCliente,ClienteComContasSchema
from app.database.session import get_db
from typing import List

router = APIRouter()

@router.get(
    '/{cliente_id}',
    summary='Mostra dados do usuario e suas contas',
    response_model=ClienteComContasSchema,
    status_code=status.HTTP_200_OK
)
def retornar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404,detail='Cliente nao encontrado')
    return cliente


@router.post(
    '/',
    summary='Criar cliente',
    response_model=ClienteOut,
    status_code=status.HTTP_201_CREATED
)
def enviar(criar: CriarCliente,db: Session = Depends(get_db)):
    novo_cliente = Cliente(**criar.model_dump())
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente


@router.get(
    '/',
    summary='Retornar todos os clientes',
    response_model=List[ClienteOut],
    status_code=status.HTTP_200_OK
)
def receber(db: Session = Depends(get_db)):
    clientes = db.query(Cliente).all()
    return clientes

@router.put(
    '/{id}',
    summary='Trocar dados do cliente',
    response_model=ClienteOut,
    status_code=status.HTTP_200_OK
)
def trocar(id: int,at: AtualizarCliente,db: Session = Depends(get_db)):
    dados_a_serem_trocados_do_cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if not dados_a_serem_trocados_do_cliente:
        raise HTTPException(status_code=404,detail='Cliente nao encontrado')
    
    if at.nome is not None:
        dados_a_serem_trocados_do_cliente.nome = at.nome
    if at.idade is not None:
        dados_a_serem_trocados_do_cliente.idade = at.idade

    db.commit()
    db.refresh(dados_a_serem_trocados_do_cliente)
    return dados_a_serem_trocados_do_cliente


@router.delete(
    '/{id}',
    summary='Deletar um cliente',
    status_code=status.HTTP_200_OK
)
def deletar(id: int,db: Session = Depends(get_db)):
    dados_a_serem_apagados_do_cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if not dados_a_serem_apagados_do_cliente:
        raise HTTPException(status_code=404,detail='Cliente nao encontrado')
    
    db.delete(dados_a_serem_apagados_do_cliente)
    db.commit()
    return {'mensagem':'Cliente deletado com sucesso'}
