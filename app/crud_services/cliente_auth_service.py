from sqlalchemy.orm import Session
from app.models.cliente_model import Cliente
from app.schemas.cliente_schema import CriarCliente, ClienteOut

class ClienteService:
    """
    Camada de serviço responsável por operações relacionadas ao Cliente.
    Mantém a lógica de persistência isolada dos controladores (rotas).
    """

    @staticmethod
    def criar_cliente_auth(criar: CriarCliente, db: Session) -> ClienteOut:
        """
        Cria um novo cliente no banco de dados a partir do schema de entrada.
        - `criar`: dados validados pelo Pydantic (CriarCliente).
        - `db`: sessão ativa do SQLAlchemy.
        Retorna o cliente recém-criado como schema de saída (ClienteOut).
        """
        novo_cliente = Cliente(**criar.model_dump())  # converte schema em dict e instancia modelo
        db.add(novo_cliente)                         # adiciona à sessão
        db.commit()                                  # persiste no banco
        db.refresh(novo_cliente)                     # atualiza objeto com dados do banco (ex: id gerado)
        return novo_cliente

    @staticmethod
    def listar_clientes_auth(db: Session) -> list[ClienteOut]:
        """
        Lista todos os clientes cadastrados.
        - `db`: sessão ativa do SQLAlchemy.
        Retorna uma lista de schemas de saída (ClienteOut).
        """
        clientes = db.query(Cliente).all()
        return [ClienteOut.model_validate(cliente) for cliente in clientes]
