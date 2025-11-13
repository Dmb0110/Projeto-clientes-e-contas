from fastapi import status,APIRouter,HTTPException,Depends,FastAPI
from sqlalchemy.orm import Session
from app.models.cliente_model import Cliente
from app.schemas.cliente_schema import CriarCliente,ClienteOut,AtualizarCliente,DeletarCliente,ClienteComContasSchema
from app.database.session import get_db
from typing import List

router = APIRouter()

class ClienteService:
    def __init__(self,db: Session = Depends(get_db)):
        self.db = db

    def enviar(self, criar: CriarCliente) -> ClienteOut:
        novo_cliente = Cliente(**criar.model_dump())
        self.db.add(novo_cliente)
        self.db.commit()
        self.db.refresh(novo_cliente)
        return ClienteOut.model_validate(novo_cliente)
    

    def receber_todos_os_clientes(self) -> List[ClienteOut]:
        clientes = self.db.query(Cliente).all()
        return [ClienteOut.model_validate(c) for c in clientes]    


    def receber_cliente_conta(self,cliente_id: int) -> ClienteComContasSchema:
        cliente = self.db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not cliente:
            raise HTTPException(status_code=404,detail='Cliente nao encontrado')
        return ClienteComContasSchema.model_validate(cliente)
    
    
    def trocar_cliente(self,cliente_id: int,at: AtualizarCliente) -> ClienteOut:
        dados_a_serem_trocados_do_cliente = self.db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not dados_a_serem_trocados_do_cliente:
            raise HTTPException(status_code=404,detail='Cliente nao encontrado')
    
        if at.nome is not None:
            dados_a_serem_trocados_do_cliente.nome = at.nome
        if at.idade is not None:
            dados_a_serem_trocados_do_cliente.idade = at.idade

        self.db.commit()
        self.db.refresh(dados_a_serem_trocados_do_cliente)
        return dados_a_serem_trocados_do_cliente
    
    
    def deletar_cliente(self,cliente_id: int) -> dict:
        dados_a_serem_apagados_do_cliente = self.db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not dados_a_serem_apagados_do_cliente:
            raise HTTPException(status_code=404,detail='Cliente nao encontrado')
    
        self.db.delete(dados_a_serem_apagados_do_cliente)
        self.db.commit()
        return {'mensagem':'Cliente deletado com sucesso'}


'''
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

def enviar(self.criar: CriarCliente) -> ClienteOut:
    novo_cliente = Cliente(**criar.model_dump())
    self.db.add(novo_cliente)
    self.db.commit()
    self.db.refresh(novo_cliente)
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

def deletar_cliente(id: int,db: Session = Depends(get_db)):
    dados_a_serem_apagados_do_cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if not dados_a_serem_apagados_do_cliente:
        raise HTTPException(status_code=404,detail='Cliente nao encontrado')
    
    db.delete(dados_a_serem_apagados_do_cliente)
    db.commit()
    return {'mensagem':'Cliente deletado com sucesso'}
'''
