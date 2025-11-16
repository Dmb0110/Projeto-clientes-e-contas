from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from app.schemas.conta_schema import ContaOut

class CriarUsuario(BaseModel):
    """
    Schema para criação de usuário.
    Usado no registro de novos usuários.
    """
    username: str
    password: str

class LoginUsuario(BaseModel):
    """
    Schema para login de usuário.
    Usado na autenticação e geração de token JWT.
    """
    username: str
    password: str

class CriarCliente(BaseModel):
    """
    Schema para criação de cliente.
    Usado na rota POST /cliente.
    """
    nome: str
    idade: int

class ClienteOut(BaseModel):
    """
    Schema de saída para cliente.
    Inclui id, nome e idade.
    """
    id: int
    nome: str
    idade: int

    # Permite criar instâncias a partir de objetos ORM (SQLAlchemy)
    model_config = ConfigDict(from_attributes=True)

class ClienteComContasSchema(BaseModel):
    """
    Schema de saída para cliente com suas contas.
    Inclui lista de ContaOut.
    """
    id: int
    nome: str
    idade: int
    contas: List[ContaOut] = []

    model_config = ConfigDict(from_attributes=True)

class AtualizarCliente(BaseModel):
    """
    Schema para atualização parcial de cliente.
    Campos opcionais permitem atualização seletiva.
    """
    nome: Optional[str] = None
    idade: Optional[int] = None

class DeletarCliente(BaseModel):
    """
    Schema de resposta para deleção de cliente.
    Retorna mensagem de confirmação.
    """
    mensagem: str
