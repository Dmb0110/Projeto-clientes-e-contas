from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base

class Conta(Base):
    """
    Modelo ORM que representa a tabela 'conta' no banco de dados.
    - id: chave primária, com índice para buscas rápidas.
    - nome_do_banco: nome da instituição financeira.
    - numero_da_agencia: número da agência bancária.
    - numero_da_conta: número da conta bancária.
    - cliente_id: chave estrangeira referenciando a tabela 'cliente'.
    - cliente: relacionamento N:1 com Cliente (cada conta pertence a um cliente).
    """

    __tablename__ = "conta"

    id = Column(Integer, primary_key=True, index=True)
    nome_do_banco = Column(String)
    numero_da_agencia = Column(Integer)
    numero_da_conta = Column(Integer)

    # Chave estrangeira que conecta Conta → Cliente
    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=True)

    # Relacionamento bidirecional com Cliente
    # back_populates='contas' → conecta com o atributo 'contas' definido em Cliente
    cliente = relationship("Cliente", back_populates="contas")
