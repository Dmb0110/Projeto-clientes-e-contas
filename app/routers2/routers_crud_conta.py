from fastapi import APIRouter, Depends, status
from app.crud_services.conta_service import ContaService
from app.schemas import CriarConta, ContaOut, AtualizarConta, DeletarConta
from typing import List

# Prefixo '/conta' → todas as rotas começam com /conta
router = APIRouter()


@router.get(
        '/health/',
        summary='Verifica status da api',
        status_code=status.HTTP_200_OK
)
def health_check():
    # Endpoint simples de health check, útil para monitoramento e integração com ferramentas de observabilidade.
    return {'Status': 'Ola desenvolvedor,tudo ok por aqui'}


@router.post(
    "/",
    summary="Criar conta",
    response_model=ContaOut,
    status_code=status.HTTP_201_CREATED
)
def criar_conta(criar: CriarConta, service: ContaService = Depends()):
    """
    Cria uma nova conta.
    - `criar`: dados validados pelo schema CriarConta.
    - `service`: instância de ContaService injetada via Depends.
    Retorna a conta criada como ContaOut.
    """
    return service.enviar(criar)

@router.get(
    "/",
    summary="Retornar todas as contas",
    response_model=List[ContaOut],
    status_code=status.HTTP_200_OK
)
def receber(service: ContaService = Depends()):
    """
    Lista todas as contas cadastradas.
    Retorna uma lista de ContaOut.
    """
    return service.receber_todas_as_contas()

@router.get(
    "/{conta_id}",
    summary="Mostra uma conta específica",
    response_model=ContaOut,
    status_code=status.HTTP_200_OK
)
def receber_um(conta_id: int, service: ContaService = Depends()):
    """
    Busca uma conta pelo ID.
    Lança 404 se não encontrada.
    Retorna a conta como ContaOut.
    """
    return service.receber_conta_especifica(conta_id)

@router.put(
    "/{conta_id}",
    summary="Trocar dados da conta",
    response_model=ContaOut,
    status_code=status.HTTP_200_OK
)
def trocar(conta_id: int, at: AtualizarConta, service: ContaService = Depends()):
    """
    Atualiza dados de uma conta existente.
    - `conta_id`: identificador da conta.
    - `at`: schema com campos opcionais para atualização.
    Retorna a conta atualizada como ContaOut.
    """
    return service.trocar_conta(conta_id, at)

@router.delete(
    "/{conta_id}",
    summary="Deletar uma conta",
    status_code=status.HTTP_200_OK
)
def deletar(conta_id: int, service: ContaService = Depends()):
    """
    Remove uma conta do banco de dados.
    Retorna mensagem de sucesso ou lança 404 se não encontrada.
    """
    return service.deletar_conta(conta_id)
