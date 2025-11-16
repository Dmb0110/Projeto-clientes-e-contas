from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from app.database.session import Base

# Caso não estivesse importando Base do projeto, poderíamos usar:
# Base = declarative_base()

class Usuario(Base):
    """
    Modelo ORM que representa a tabela 'usuario' no banco de dados.
    - id: chave primária, com índice para buscas rápidas.
    - username: nome de login do usuário.
    - password: senha criptografada do usuário.
    """

    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
