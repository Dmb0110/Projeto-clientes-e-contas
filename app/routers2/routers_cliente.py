from fastapi import APIRouter,Depends,status
from app.crud_services.cliente_service import ClienteService
from app.schemas import CriarCliente,ClienteOut,ClienteComContasSchema,AtualizarCliente
from typing import List

router = APIRouter(prefix='/cliente')

@router.post(
    '/',
    summary='Criar cliente',
    response_model=ClienteOut,
    status_code=status.HTTP_201_CREATED
)
def criar_cliente(criar: CriarCliente,service: ClienteService = Depends()):
    return service.enviar(criar)
    

@router.get(
    '/',
    summary='Retornar todos os clientes',
    response_model=List[ClienteOut],
    status_code=status.HTTP_200_OK
)
def receber(service: ClienteService = Depends()):
    return service.receber_todos_os_clientes()


@router.get(
    '/{cliente_id}',
    summary='Mostra dados do usuario e suas contas',
    response_model=ClienteComContasSchema,
    status_code=status.HTTP_200_OK
)
def receber_cliente_conta(cliente_id: int,service: ClienteService = Depends()):
    return service.receber_cliente_conta(cliente_id)


@router.put(
    '/{cliente_id}',
    summary='Trocar dados do cliente',
    response_model=ClienteOut,
    status_code=status.HTTP_200_OK
)
def trocar(cliente_id: int,at: AtualizarCliente,service: ClienteService = Depends()):
    return service.trocar_cliente(cliente_id,at)


@router.delete(
    '/{cliente_id}',
    summary='Deletar um cliente',
    status_code=status.HTTP_200_OK
)
def deletar(cliente_id: int,service: ClienteService = Depends()):
    return service.deletar_cliente(cliente_id)

