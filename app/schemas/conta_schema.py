from typing import Optional
from pydantic import BaseModel, ConfigDict,Field

class CriarConta(BaseModel):
    """
    Schema de entrada para criação de conta.
    Usado na rota POST /conta.
    """
    nome_do_banco: str = Field(..., min_length=3, max_length=100)
    numero_da_agencia: int = Field(..., ge=1)
    numero_da_conta: int = Field(..., ge=1)
    cliente_id: Optional[int] = None  # permite criar conta sem cliente associado

class ContaOut(BaseModel):
    """
    Schema de saída para conta.
    Inclui id e dados básicos da conta.
    """
    id: int
    nome_do_banco: str
    numero_da_agencia: int
    numero_da_conta: int
    cliente_id: Optional[int] = None

    # Permite instanciar diretamente a partir de objetos ORM (SQLAlchemy)
    model_config = ConfigDict(from_attributes=True)

class AtualizarConta(BaseModel):
    """
    Schema para atualização parcial de conta.
    Campos opcionais permitem atualização seletiva.
    """
    nome_do_banco: Optional[str] = Field(None, min_length=3, max_length=100)
    numero_da_agencia: Optional[int] = Field(None, ge=1)
    numero_da_conta: Optional[int] = Field(None, ge=1)

class DeletarConta(BaseModel):
    """
    Schema de resposta para deleção de conta.
    Retorna mensagem de confirmação.
    """
    mensagem: str
