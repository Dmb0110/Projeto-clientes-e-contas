
'''
from fastapi import APIRouter,HTTPException,Depends,FastAPI
from sqlalchemy.orm import Session
from app.models.conta_model import Conta
from app.schemas.conta_schema import CriarConta,ContaOut,AtualizarConta,DeletarConta
from app.database.session import get_db
from typing import List

router = APIRouter()

@router.post(
    '/',
    summary='Criar conta',
    response_model=ContaOut
)
def enviar(criar: CriarConta,db: Session = Depends(get_db)):
    novo_cliente = Conta(**criar.dict())
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente


@router.get(
    '/',
    summary='Retornar todos as contas',
    response_model=List[ContaOut]
)
def receber(db: Session = Depends(get_db)):
    return db.query(Conta).all()


@router.put(
    '/{id}',
    summary='Trocar dados da conta',
    response_model=ContaOut
)
def trocar(id: int,at: AtualizarConta,db: Session = Depends(get_db)):
    dados_a_serem_trocados_da_conta_do_cliente = db.query(Conta).filter(Conta.id == id).first()
    if not dados_a_serem_trocados_da_conta_do_cliente:
        raise HTTPException(status_code=404,detail='Conta nao encontrada')
    
    if at.nome_do_banco is not None:
        dados_a_serem_trocados_da_conta_do_cliente.nome_do_banco = at.nome_do_banco
    if at.numero_da_agencia is not None:
        dados_a_serem_trocados_da_conta_do_cliente.numero_da_agencia = at.numero_da_agencia
    if at.numero_da_conta is not None:
        dados_a_serem_trocados_da_conta_do_cliente.numero_da_conta = at.numero_da_conta

    db.commit()
    db.refresh(dados_a_serem_trocados_da_conta_do_cliente)
    return dados_a_serem_trocados_da_conta_do_cliente


@router.delete(
    '/{id}',
    summary='Deletar um uma conta'
)
def trocar(id: int,db: Session = Depends(get_db)):
    dados_a_serem_apagados_da_conta_do_cliente = db.query(Conta).filter(Conta.id == id).first()
    if not dados_a_serem_apagados_da_conta_do_cliente:
        raise HTTPException(status_code=404,detail='Conta nao encontrado')
    
    db.delete(dados_a_serem_apagados_da_conta_do_cliente)
    db.commit()
    return {'mensagem':'Conta do cliente deletada com sucesso'}
'''





from fastapi import status,APIRouter,HTTPException,Depends,FastAPI
from sqlalchemy.orm import Session
from app.models.conta_model import Conta
from app.models.cliente_model import Cliente
from app.schemas.conta_schema import CriarConta,ContaOut,AtualizarConta,DeletarConta
from app.database.session import get_db
from typing import List

router = APIRouter()

class ContaService:
    def __init__(self,db: Session = Depends(get_db)):
        self.db = db

    def enviar(self, criar: CriarConta) -> ContaOut:
        if criar.cliente_id is not None:
            cliente = self.db.query(Cliente).filter(Cliente.id == criar.cliente_id).first()
            if not cliente:
                raise HTTPException(status_code=400,detail='Cliente nao encontrado')
        
        novo_conta = Conta(**criar.model_dump())
        self.db.add(novo_conta)
        self.db.commit()
        self.db.refresh(novo_conta)
        return ContaOut.model_validate(novo_conta)
    

    def receber_todas_as_contas(self) -> List[ContaOut]:
        contas = self.db.query(Conta).all()
        return [ContaOut.model_validate(c) for c in contas]    


    def receber_conta_especifica(self,conta_id: int) -> ContaOut:
        conta = self.db.query(Conta).filter(Conta.id == conta_id).first()
        if not conta:
            raise HTTPException(status_code=404,detail='Conta nao encontrada')
        return ContaOut.model_validate(conta)
    
    
    def trocar_conta(self,conta_id: int,at: AtualizarConta) -> ContaOut:
        dados_da_conta = self.db.query(Conta).filter(Conta.id == conta_id).first()
        if not dados_da_conta:
            raise HTTPException(status_code=404,detail='Conta nao encontrada')
    
        if at.nome_do_banco is not None:
            dados_da_conta.nome_do_banco = at.nome_do_banco
        if at.numero_da_agencia is not None:
            dados_da_conta.numero_da_agencia = at.numero_da_agencia
        if at.numero_da_conta is not None:
            dados_da_conta.numero_da_conta = at.numero_da_conta

        self.db.commit()
        self.db.refresh(dados_da_conta)
        return dados_da_conta
    
    
    def deletar_conta(self,conta_id: int) -> dict:
        dados_da_conta = self.db.query(Conta).filter(Conta.id == conta_id).first()
        if not dados_da_conta:
            raise HTTPException(status_code=404,detail='Conta nao encontrada')
    
        self.db.delete(dados_da_conta)
        self.db.commit()
        return {'mensagem':'Conta deletada com sucesso'}

