from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base

class Conta(Base):
    __tablename__ = 'conta'

    id = Column(Integer,primary_key=True,index=True)
    nome_do_banco = Column(String)
    numero_da_agencia = Column(Integer)
    numero_da_conta = Column(Integer)
    
    cliente_id = Column(Integer,ForeignKey('cliente.id'),nullable=True)
    cliente = relationship('Cliente',back_populates='contas')
