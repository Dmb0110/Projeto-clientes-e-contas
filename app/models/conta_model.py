from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship,Mapped,mapped_column
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

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome_do_banco: Mapped[str] = mapped_column(String(100),nullable=False)
    numero_da_agencia: Mapped[str] = mapped_column(Integer, nullable=False)
    numero_da_conta: Mapped[str] = mapped_column(Integer, nullable=False)

    # Chave estrangeira que conecta Conta → Cliente
    cliente_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("cliente.id", ondelete='CASCADE'), nullable=True
    )

    # Relacionamento bidirecional com Cliente
    # back_populates='contas' → conecta com o atributo 'contas' definido em Cliente
    cliente: Mapped['Cliente'] = relationship(
        "Cliente",
        back_populates="contas",
        lazy='joined'
    )
