from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models_usuario.usuario import Usuario
from app.schemas.cliente_schema import CriarUsuario
from passlib.context import CryptContext

# Configuração do contexto de criptografia para senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class RegistroService:
    """
    Serviço responsável pelo registro de novos usuários.
    - Verifica se o usuário já existe.
    - Criptografa a senha com bcrypt.
    - Persiste o usuário no banco de dados.
    """

    @staticmethod
    def registrar_usuario(request: CriarUsuario, db: Session) -> dict:
        """
        Registra um novo usuário no sistema.
        - `request`: schema Pydantic com username e password.
        - `db`: sessão ativa do SQLAlchemy.
        
        Fluxo:
        1. Verifica se o username já existe.
        2. Criptografa a senha com bcrypt.
        3. Cria e salva o usuário no banco.
        4. Retorna mensagem de sucesso.
        """
        # Verifica se o usuário já existe
        usuario_existente = db.query(Usuario).filter(Usuario.username == request.username).first()
        if usuario_existente:
            raise HTTPException(status_code=400, detail="Usuário já existe")

        # Criptografa a senha
        senha_hash = pwd_context.hash(request.password)

        # Cria e salva o novo usuário
        novo_usuario = Usuario(username=request.username, password=senha_hash)
        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)  # garante que atributos gerados (ex: id) sejam carregados

        return {"mensagem": "Usuário registrado com sucesso"}
