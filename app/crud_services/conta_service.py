from fastapi import status, APIRouter, HTTPException, Depends, FastAPI
from sqlalchemy.orm import Session
from app.models.conta_model import Conta
from app.models.cliente_model import Cliente
from app.schemas.conta_schema import CriarConta, ContaOut, AtualizarConta, DeletarConta
from app.database.session import get_db
from typing import List

router = APIRouter()

class ContaService:
    """
    Camada de serviço responsável pelas operações CRUD relacionadas à Conta.
    Usa SQLAlchemy para persistência e schemas Pydantic para entrada/saída.
    """

    def __init__(self, db: Session = Depends(get_db)):
        # Injeta a sessão do banco via FastAPI Depends
        self.db = db

    def enviar(self, criar: CriarConta) -> ContaOut:
        """
        Cria uma nova conta no banco de dados.
        - `criar`: dados validados pelo schema CriarConta.
        Valida se o cliente existe antes de criar a conta.
        Retorna a conta criada como ContaOut.
        """
        if criar.cliente_id is not None:
            cliente = self.db.query(Cliente).filter(Cliente.id == criar.cliente_id).first()
            if not cliente:
                raise HTTPException(status_code=400, detail="Cliente não encontrado")
        
        nova_conta = Conta(**criar.model_dump())
        self.db.add(nova_conta)
        self.db.commit()
        self.db.refresh(nova_conta)  # garante que atributos gerados (ex: id) sejam carregados
        return ContaOut.model_validate(nova_conta)

    def receber_todas_as_contas(self) -> List[ContaOut]:
        """
        Retorna todas as contas cadastradas.
        """
        contas = self.db.query(Conta).all()
        return [ContaOut.model_validate(c) for c in contas]

    def receber_conta_especifica(self, conta_id: int) -> ContaOut:
        """
        Busca uma conta pelo ID.
        Lança 404 se não encontrada.
        """
        conta = self.db.query(Conta).filter(Conta.id == conta_id).first()
        if not conta:
            raise HTTPException(status_code=404, detail="Conta não encontrada")
        return ContaOut.model_validate(conta)

    def trocar_conta(self, conta_id: int, at: AtualizarConta) -> ContaOut:
        """
        Atualiza dados de uma conta existente.
        - `conta_id`: identificador da conta.
        - `at`: schema com campos opcionais para atualização.
        """
        dados_da_conta = self.db.query(Conta).filter(Conta.id == conta_id).first()
        if not dados_da_conta:
            raise HTTPException(status_code=404, detail="Conta não encontrada")
    
        if at.nome_do_banco is not None:
            dados_da_conta.nome_do_banco = at.nome_do_banco
        if at.numero_da_agencia is not None:
            dados_da_conta.numero_da_agencia = at.numero_da_agencia
        if at.numero_da_conta is not None:
            dados_da_conta.numero_da_conta = at.numero_da_conta

        self.db.commit()
        self.db.refresh(dados_da_conta)
        return dados_da_conta

    def deletar_conta(self, conta_id: int) -> dict:
        """
        Remove uma conta do banco.
        Retorna mensagem de sucesso ou lança 404 se não encontrada.
        """
        dados_da_conta = self.db.query(Conta).filter(Conta.id == conta_id).first()
        if not dados_da_conta:
            raise HTTPException(status_code=404, detail="Conta não encontrada")
    
        self.db.delete(dados_da_conta)
        self.db.commit()
        return {"mensagem": "Conta deletada com sucesso"}
