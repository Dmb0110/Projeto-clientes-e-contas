from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from app.schemas.conta_schema import CriarConta,ContaOut
from app.database.session import get_db
from app.auth.jwt import verificar_token
from app.crud_services.conta_auth_service import ContaService

router = APIRouter()

@router.post(
    "/",
    summary="Rota protagida Criar cliente",
    response_model=ContaOut,
    status_code=status.HTTP_201_CREATED
)
def criar_Conta(
    criar: CriarConta,
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):
    return ContaService.criar_conta_auth(criar,db)
    

@router.get(
    "/",
    summary='Rota protegida quer retorna todos os usuarios',
    response_model=list[ContaOut],
    status_code=status.HTTP_200_OK
)
def listar_contas(
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):
    return ContaService.listar_contas_auth(db)
    