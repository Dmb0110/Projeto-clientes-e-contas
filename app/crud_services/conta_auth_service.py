from app.schemas.conta_schema import CriarConta,ContaOut
from app.models.conta_model import Conta
from sqlalchemy.orm import Session
from app.database.session import get_db

class ContaService:

    @staticmethod
    def criar_conta_auth(criar: CriarConta,db: Session) -> ContaOut:
        nova_conta = Conta(**criar.model_dump())
        db.add(nova_conta)
        db.commit()
        db.refresh(nova_conta)
        return nova_conta
    
    @staticmethod
    def listar_contas_auth(db: Session) -> list[ContaOut]:
        clientes = db.query(Conta).all()
        return [ContaOut.model_validate(cliente) for cliente in clientes]
