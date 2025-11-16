from fastapi import status, APIRouter, HTTPException, Depends, FastAPI
from sqlalchemy.orm import Session
from app.models.cliente_model import Cliente
from app.schemas.cliente_schema import (
    CriarCliente, ClienteOut, AtualizarCliente, DeletarCliente, ClienteComContasSchema
)
from app.database.session import get_db
from typing import List

router = APIRouter()

class ClienteService:
    """
    Camada de serviço responsável pelas operações CRUD relacionadas ao Cliente.
    Usa SQLAlchemy para persistência e schemas Pydantic para entrada/saída.
    """

    def __init__(self, db: Session = Depends(get_db)):
        # Injeta a sessão do banco via FastAPI Depends
        self.db = db

    def enviar(self, criar: CriarCliente) -> ClienteOut:
        """
        Cria um novo cliente no banco.
        - `criar`: dados validados pelo schema CriarCliente.
        Retorna o cliente criado como ClienteOut.
        """
        novo_cliente = Cliente(**criar.model_dump())
        self.db.add(novo_cliente)
        self.db.commit()
        self.db.refresh(novo_cliente)  # garante que atributos gerados (ex: id) sejam carregados
        return ClienteOut.model_validate(novo_cliente)

    def receber_todos_os_clientes(self) -> List[ClienteOut]:
        """
        Retorna todos os clientes cadastrados.
        """
        clientes = self.db.query(Cliente).all()
        return [ClienteOut.model_validate(c) for c in clientes]

    def receber_cliente_conta(self, cliente_id: int) -> ClienteComContasSchema:
        """
        Busca um cliente pelo ID e retorna junto com suas contas.
        Lança 404 se não encontrado.
        """
        cliente = self.db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not cliente:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        return ClienteComContasSchema.model_validate(cliente)

    def trocar_cliente(self, cliente_id: int, at: AtualizarCliente) -> ClienteOut:
        """
        Atualiza dados de um cliente existente.
        - `cliente_id`: identificador do cliente.
        - `at`: schema com campos opcionais para atualização.
        """
        dados_a_serem_trocados_do_cliente = self.db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not dados_a_serem_trocados_do_cliente:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")

        if at.nome is not None:
            dados_a_serem_trocados_do_cliente.nome = at.nome
        if at.idade is not None:
            dados_a_serem_trocados_do_cliente.idade = at.idade

        self.db.commit()
        self.db.refresh(dados_a_serem_trocados_do_cliente)
        return dados_a_serem_trocados_do_cliente

    def deletar_cliente(self, cliente_id: int) -> dict:
        """
        Remove um cliente do banco.
        Retorna mensagem de sucesso ou lança 404 se não encontrado.
        """
        dados_a_serem_apagados_do_cliente = self.db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not dados_a_serem_apagados_do_cliente:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")

        self.db.delete(dados_a_serem_apagados_do_cliente)
        self.db.commit()
        return {"mensagem": "Cliente deletado com sucesso"}

