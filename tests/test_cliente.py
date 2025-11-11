'''

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_listar_clientes():
    response = client.get("/cliente")
    assert response.status_code == 200
    print('teste realizado com sucesso')


import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_listar_clientes():
    response = client.get("/cliente")
    assert response.status_code == 200
    
    # pega todos os registros retornados pelo endpoint
    data = response.json()
    print("\nContas do banco:", data)   # imprime no terminal
    
    # valida que é uma lista
    assert isinstance(data, list)

    print('\n [Teste de listar as contas bem sucedido.]')

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get():
    response = client.get("/cliente")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data,list)
    assert len(data) > 0
    #assert response.json()[0]["nome_do_banco"] == "bradesco"
    print('\n Teste bem sucedido,dados retornados:',data)


from fastapi.testclient import TestClient
from app.main import app
from app.auth.jwt import create_access_token  # ou onde estiver sua função

client = TestClient(app)

def test_rota_protegida():
    token = create_access_token(data={"sub": "usuario_teste"})
    headers = {"Authorization": f"Bearer {eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbjEiLCJleHAiOjE3NjI4MTgyODl9.3ENZvPWTvX0y-LNwB8Ww2mVcctHFlscl1bRoYJLUjpo}"}

    response = client.get("/cliente_auth", headers=headers)
    assert response.status_code == 200
    assert "mensagem" in response.json()




from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_rota_protegida():
    # Token JWT válido (exemplo fixo — idealmente gerado dinamicamente)
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbjEiLCJleHAiOjE3NjI4MTgyODl9.3ENZvPWTvX0y-LNwB8Ww2mVcctHFlscl1bRoYJLUjpo"
    headers = {"Authorization": f"Bearer {token}"}

    # Faz a requisição à rota protegida
    response = client.get("/cliente_auth", headers=headers)

    # Verifica se a resposta foi bem-sucedida
    assert response.status_code == 200

    # Verifica se a resposta contém a chave esperada
    data = response.json()
    assert "mensagem" in data

    # Imprime mensagem de sucesso
    print("\n✅ Teste bem-sucedido: rota protegida respondeu com:", data["mensagem"])






from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_rota_privada_token_valido():
    headers = {"Authorization": "Bearer meu_token_teste"}
    response = client.get("/usuarios/me", headers=headers)

    assert response.status_code == 200
    assert response.json()["username"] == "david"
'''


