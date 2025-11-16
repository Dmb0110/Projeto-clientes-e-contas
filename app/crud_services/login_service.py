from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from app.schemas.cliente_schema import LoginUsuario
from app.database.session import get_db
from app.auth.jwt import authenticate_user, create_token

class LoginService:
    """
    Serviço responsável pela autenticação de usuários.
    - Recebe credenciais (username, password).
    - Valida contra o banco de dados.
    - Gera e retorna um token JWT em caso de sucesso.
    """

    @staticmethod
    def login(request: LoginUsuario, db: Session = Depends(get_db)):
        """
        Realiza o processo de login:
        1. Extrai username e password do schema de entrada.
        2. Autentica o usuário usando a função `authenticate_user`.
        3. Se inválido, lança HTTP 401.
        4. Se válido, gera um JWT com `create_token`.

        Retorna um dicionário com o access_token.
        """
        username = request.username
        password = request.password

        user = authenticate_user(db, username, password)
        if not user:
            raise HTTPException(status_code=401, detail="Credenciais inválidas")

        token = create_token({"sub": username})  # payload inclui o "sub" (subject) como username
        return {"access_token": token}
