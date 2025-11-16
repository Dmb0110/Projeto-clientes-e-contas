from app.schemas.conta_schema import CriarConta, ContaOut
from app.models.conta_model import Conta
from sqlalchemy.orm import Session
from app.database.session import get_db

class ContaService:
    """
    Camada de serviço responsável pelas operações relacionadas à Conta.
    Usa SQLAlchemy para persistência e schemas Pydantic para entrada/saída.
    """

    @staticmethod
    def criar_conta_auth(criar: CriarConta, db: Session) -> ContaOut:
        """
        Cria uma nova conta no banco de dados.
        - `criar`: dados validados pelo schema CriarConta.
        - `db`: sessão ativa do SQLAlchemy.
        Retorna a conta criada como schema de saída (ContaOut).
        """
        nova_conta = Conta(**criar.model_dump())  # converte schema em dict e instancia modelo
        db.add(nova_conta)
        db.commit()
        db.refresh(nova_conta)  # atualiza objeto com dados persistidos (ex: id gerado)
        return nova_conta

    @staticmethod
    def listar_contas_auth(db: Session) -> list[ContaOut]:
        """
        Lista todas as contas cadastradas.
        - `db`: sessão ativa do SQLAlchemy.
        Retorna uma lista de schemas de saída (ContaOut).
        """
        contas = db.query(Conta).all()
        return [ContaOut.model_validate(conta) for conta in contas]
