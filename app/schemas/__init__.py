from .cliente_schema import CriarCliente, ClienteOut, ClienteComContasSchema, AtualizarCliente
from .conta_schema import CriarConta, ContaOut, AtualizarConta, DeletarConta

# __all__ define explicitamente quais símbolos serão exportados
# quando alguém fizer "from app.schemas import *"
__all__ = [
    "CriarCliente",
    "ClienteOut",
    "ClienteComContasSchema",
    "AtualizarCliente",
    "CriarConta",
    "ContaOut",
    "AtualizarConta",
    "DeletarConta",
]
