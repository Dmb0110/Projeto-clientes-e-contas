from typing import Optional, List
from pydantic import BaseModel, ConfigDict,Field
from app.schemas.conta_schema import ContaOut

class CriarUsuario(BaseModel):
    """
    Schema para criação de usuário.
    Usado no registro de novos usuários.
    """
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=2)

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
    nome: str = Field(..., min_length=3, max_length=100)
    idade: int = Field(..., ge=0,le=120)

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
    nome: Optional[str] = Field(None, min_length=3, max_length=100)
    idade: Optional[int] = Field(None, ge=0,le=120)

class DeletarCliente(BaseModel):
    """
    Schema de resposta para deleção de cliente.
    Retorna mensagem de confirmação.
    """
    mensagem: str
