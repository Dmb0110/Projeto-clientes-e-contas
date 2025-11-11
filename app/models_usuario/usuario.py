from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base
from app.database.session import Base

#Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String)
    password = Column(String)
