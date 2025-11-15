from sqlalchemy.orm import Session
from app.models.cliente_model import Cliente
from app.schemas.cliente_schema import CriarCliente,ClienteOut

class ClienteService:

    @staticmethod
    def criar_cliente_auth(criar: CriarCliente,db: Session) -> ClienteOut:
        novo_cliente = Cliente(**criar.model_dump())
        db.add(novo_cliente)
        db.commit()
        db.refresh(novo_cliente)
        return novo_cliente
    
    @staticmethod
    def listar_clientes_auth(db: Session) -> list[ClienteOut]:
        clientes = db.query(Cliente).all()
        return [ClienteOut.model_validate(cliente) for cliente in clientes]
