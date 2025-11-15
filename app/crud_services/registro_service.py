

from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models_usuario.usuario import Usuario
from app.schemas.cliente_schema import CriarUsuario
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class RegistroService:

    @staticmethod
    def registrar_usuario(request: CriarUsuario, db: Session) -> dict:
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
        db.refresh(novo_usuario)

        return {"mensagem": "Usuário registrado com sucesso"}
    
