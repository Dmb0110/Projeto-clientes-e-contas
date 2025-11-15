from sqlalchemy.orm import Session
from fastapi import HTTPException,Depends
from app.schemas.cliente_schema import LoginUsuario
from app.database.session import get_db
from app.auth.jwt import authenticate_user,create_token

class LoginService:

    @staticmethod
    def login(request: LoginUsuario,db: Session = Depends(get_db)):
        username = request.username
        password = request.password

        user = authenticate_user(db,username,password)
        if not user:
            raise HTTPException(status_code=401, detail="Credenciais inválidas")

        token = create_token({"sub": username})
        return {"access_token": token}
    
