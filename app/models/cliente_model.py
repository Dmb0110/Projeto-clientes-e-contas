from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.session import Base

class Cliente(Base):
    """
    Modelo ORM que representa a tabela 'cliente' no banco de dados.
    - id: chave primária, com índice para buscas rápidas.
    - nome: nome do cliente.
    - idade: idade do cliente.
    - contas: relacionamento 1:N com a tabela Conta.
    """

    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    idade = Column(Integer)

    # Define relacionamento com a entidade Conta
    # back_populates='cliente' → conecta com o atributo 'cliente' definido em Conta
    contas = relationship("Conta", back_populates="cliente")
