from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped,mapped_column, relationship
from app.database.session import Base
from typing import List,Optional
#from app.models.models_conta import Conta

class Cliente(Base):
    """
    Modelo ORM que representa a tabela 'cliente' no banco de dados.
    - id: chave primária, com índice para buscas rápidas.
    - nome: nome do cliente.
    - idade: idade do cliente.
    - contas: relacionamento 1:N com a tabela Conta.
    """

    __tablename__ = "cliente"

    id: Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    nome: Mapped[str] = mapped_column(String(100),nullable=False)
    idade: Mapped[int] = mapped_column(Integer,nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String(100),nullable=True)

    # Define relacionamento com a entidade Conta
    # back_populates='cliente' → conecta com o atributo 'cliente' definido em Conta
    contas: Mapped[List['Conta']] = relationship(
        'Conta',
        back_populates='cliente',
        cascade='all, delete-orphan'
    )
    
    #contas = relationship("Conta", back_populates="cliente")
