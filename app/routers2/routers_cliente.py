from fastapi import APIRouter, Depends, status
from app.crud_services.cliente_service import ClienteService
from app.schemas import CriarCliente, ClienteOut, ClienteComContasSchema, AtualizarCliente
from typing import List

# Prefixo '/cliente' → todas as rotas começam com /cliente
router = APIRouter(prefix="/cliente")

@router.post(
    "/",
    summary="Criar cliente",
    response_model=ClienteOut,
    status_code=status.HTTP_201_CREATED
)
def criar_cliente(criar: CriarCliente, service: ClienteService = Depends()):
    """
    Cria um novo cliente.
    - `criar`: dados validados pelo schema CriarCliente.
    - `service`: instância de ClienteService injetada via Depends.
    Retorna o cliente criado como ClienteOut.
    """
    return service.enviar(criar)

@router.get(
    "/",
    summary="Retornar todos os clientes",
    response_model=List[ClienteOut],
    status_code=status.HTTP_200_OK
)
def receber(service: ClienteService = Depends()):
    """
    Lista todos os clientes cadastrados.
    Retorna uma lista de ClienteOut.
    """
    return service.receber_todos_os_clientes()

@router.get(
    "/{cliente_id}",
    summary="Mostra dados do cliente e suas contas",
    response_model=ClienteComContasSchema,
    status_code=status.HTTP_200_OK
)
def receber_cliente_conta(cliente_id: int, service: ClienteService = Depends()):
    """
    Busca um cliente específico pelo ID e retorna junto com suas contas.
    Lança 404 se não encontrado.
    """
    return service.receber_cliente_conta(cliente_id)

@router.put(
    "/{cliente_id}",
    summary="Trocar dados do cliente",
    response_model=ClienteOut,
    status_code=status.HTTP_200_OK
)
def trocar(cliente_id: int, at: AtualizarCliente, service: ClienteService = Depends()):
    """
    Atualiza dados de um cliente existente.
    - `cliente_id`: identificador do cliente.
    - `at`: schema com campos opcionais para atualização.
    Retorna o cliente atualizado como ClienteOut.
    """
    return service.trocar_cliente(cliente_id, at)

@router.delete(
    "/{cliente_id}",
    summary="Deletar um cliente",
    status_code=status.HTTP_200_OK
)
def deletar(cliente_id: int, service: ClienteService = Depends()):
    """
    Remove um cliente do banco de dados.
    Retorna mensagem de sucesso ou lança 404 se não encontrado.
    """
    return service.deletar_cliente(cliente_id)
