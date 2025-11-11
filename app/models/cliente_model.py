from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from app.database.session import Base

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer,primary_key=True,index=True)
    nome = Column(String)
    idade = Column(Integer)
    
    contas = relationship('Conta',back_populates='cliente')
