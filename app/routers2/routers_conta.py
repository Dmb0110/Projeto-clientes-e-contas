from fastapi import APIRouter,Depends,status
from app.crud_services.conta_service import ContaService
from app.schemas import CriarConta,ContaOut,AtualizarConta,DeletarConta
from typing import List

router = APIRouter(prefix='/conta')

@router.post(
    '/',
    summary='Criar conta',
    response_model=ContaOut,
    status_code=status.HTTP_201_CREATED
)
def criar_conta(criar: CriarConta,service: ContaService = Depends()):
    return service.enviar(criar)
    

@router.get(
    '/',
    summary='Retornar todos as contas',
    response_model=List[ContaOut],
    status_code=status.HTTP_200_OK
)
def receber(service: ContaService = Depends()):
    return service.receber_todas_as_contas()


@router.get(
    '/{conta_id}',
    summary='Mostra uma conta especifica',
    response_model=ContaOut,
    status_code=status.HTTP_200_OK
)
def receber_um(conta_id: int,service: ContaService = Depends()):
    return service.receber_conta_especifica(conta_id)


@router.put(
    '/{conta_id}',
    summary='Trocar dados do conta',
    response_model=ContaOut,
    status_code=status.HTTP_200_OK
)
def trocar(conta_id: int,at: AtualizarConta,service: ContaService = Depends()):
    return service.trocar_conta(conta_id,at)


@router.delete(
    '/{conta_id}',
    summary='Deletar uma conta',
    status_code=status.HTTP_200_OK
)
def deletar(conta_id: int,service: ContaService = Depends()):
    return service.deletar_conta(conta_id)

