from typing import Optional
from pydantic import BaseModel,ConfigDict

class CriarConta(BaseModel):
    nome_do_banco: str
    numero_da_agencia: int
    numero_da_conta: int
    cliente_id: int

class ContaOut(BaseModel):
    id: int
    nome_do_banco: str
    numero_da_agencia: int
    numero_da_conta: int
    cliente_id: Optional[int] = None

    model_config = ConfigDict(
        from_attributes=True
    )

class AtualizarConta(BaseModel):
    nome_do_banco:Optional[str] = None
    numero_da_agencia:Optional[int] = None
    numero_da_conta:Optional[int] = None

class DeletarConta(BaseModel):
    mensagem: str
