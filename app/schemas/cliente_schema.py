from typing import Optional,List
from pydantic import BaseModel,ConfigDict
from app.schemas.conta_schema import ContaOut

class CriarUsuario(BaseModel):
    username: str
    password: str

class LoginUsuario(BaseModel):
    username: str
    password: str
##############################
class CriarCliente(BaseModel):
    nome: str
    idade: int

class ClienteOut(BaseModel):
    id: int
    nome: str
    idade: int

    model_config = ConfigDict(
        from_attributes=True
    )

class ClienteComContasSchema(BaseModel):
    id: int
    nome: str
    idade: int
    contas: List[ContaOut] = []

    model_config = ConfigDict(
        from_attributes=True
    )

class AtualizarCliente(BaseModel):
    nome:Optional[str] = None
    idade:Optional[int] = None

class DeletarCliente(BaseModel):
    mensagem: str
