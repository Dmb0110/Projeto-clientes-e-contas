from fastapi import Request, HTTPException, Depends,APIRouter
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import jwt, JWTError, ExpiredSignatureError
from passlib.context import CryptContext
from app.models_usuario.usuario import Usuario
from app.database.session import get_db
from app.schemas.cliente_schema import CriarUsuario,LoginUsuario
import os

router = APIRouter()

# Configurações do JWT
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Criptografia de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Verifica se a senha fornecida corresponde ao hash
def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# Cria um token JWT com tempo de expiração
def create_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Decodifica o token JWT e retorna o usuário
def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None

# Autentica o usuário verificando credenciais
def authenticate_user(db: Session, username: str, password: str):
    user = db.query(Usuario).filter(Usuario.username == username).first()
    if not user or not verify_password(password, user.password):
        return None
    return user

# Verifica se o token JWT é válido e extrai o usuário
def verificar_token(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token ausente ou mal formatado")

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return username
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

'''
# Endpoint para registrar novo usuário
@router.post(
    "/registro",
    summary='Registrar o usuario',
    status_code=201
)
async def registrar_usuario(request: CriarUsuario, db: Session = Depends(get_db)):
    #try:    # Verifica se o usuário já existe
    usuario_existente = db.query(Usuario).filter(Usuario.username == request.username).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    # Criptografa a senha
    senha_hash = pwd_context.hash(request.password)

    # Cria e salva o novo usuário
    novo_usuario = Usuario(username=request.username,password=senha_hash)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return {"mensagem": "Usuário registrado com sucesso"}

    #except Exception as e:
     #   raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")


# Endpoitn para login e geração de token
@router.post(
    "/login",
    summary='Criar login para o usuario e gerar o token'
)
async def login(request: LoginUsuario,db: Session = Depends(get_db)):
    username = request.username
    password = request.password

    user = authenticate_user(db,username,password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_token({"sub": username})
    return {"access_token": token}
'''
