from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from app.schemas.cliente_schema import CriarCliente,ClienteOut
from app.database.session import get_db
from app.auth.jwt import verificar_token
from app.crud_services.cliente_auth_service import ClienteService

router = APIRouter()

@router.post(
    "/",
    summary="Rota protagida Criar cliente",
    response_model=ClienteOut,
    status_code=status.HTTP_201_CREATED
)
def criar_cliente(
    criar: CriarCliente,
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):
    return ClienteService.criar_cliente_auth(criar,db)
    

@router.get(
    "/",
    summary='Rota protegida quer retorna todos os usuarios',
    response_model=list[ClienteOut],
    status_code=status.HTTP_200_OK
)
def listar_clientes(
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):
    return ClienteService.listar_clientes_auth(db)
    