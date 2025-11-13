
'''
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

pytest -s -v tests/test_postget_cliente.py
'''

'''
# 🔹 Fixture para obter token válido
@pytest.fixture
def token_valido():
    # Primeiro registra um usuário
    usuario = {
        "username": "clienteuser",
        "email": "cliente@example.com",
        "password": "senha123"
    }
    client.post("/register", json=usuario)

    # Faz login para obter token
    response = client.post("/login", data={
        "username": "clienteuser",
        "password": "senha123"
    })
    assert response.status_code == 200
    return response.json()["access_token"]

# 🔹 Teste da rota POST protegida (criar cliente)
def test_criar_cliente(token_valido):
    headers = {"Authorization": f"Bearer {'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbjEiLCJleHAiOjE3NjI5MTY2NTV9.sL_11kVUnliv78hBsnWtOFH5EcrepF4kX695SVis9nE'}"}
               
    novo_cliente = {"nome": "João Teste", "idade": 25}
    response = client.post("/cliente_auth", json=novo_cliente, headers=headers)
    assert response.status_code == 200 or response.status_code == 201
    data = response.json()
    assert data["nome"] == "João Teste"
   # assert "id" in data

# 🔹 Teste da rota GET protegida (listar clientes)
def test_listar_clientes(token_valido):
    headers = {"Authorization": f"Bearer {'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbjEiLCJleHAiOjE3NjI5MDQ5NzZ9.gPOH3VneQ8QDJx7-krCGnrWzRxot2GkQnmOiP6FttSw'}"}
    response = client.get("/cliente_auth", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    #assert "nome" in data[0]
'''

'''

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


pytest -s -v tests/test_postget_cliente.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def token_valido():
    # Registra um usuário
    usuario = {"username": "user_listar", "password": "123456"}
    client.post("/registro", json=usuario)

    # Faz login e pega o token
    response = client.post("/login", json=usuario)
    data = response.json()
    return data["access_token"]

def test_listar_clientes(token_valido):
    # Cria um cliente para garantir que a lista não esteja vazia
    novo_cliente = {"nome": "Maria", "idade": 30}
    client.post(
        "/cliente_auth",  # ajuste conforme o prefixo real do seu router
        json=novo_cliente,
        headers={"Authorization": f"Bearer {token_valido}"}
    )

    # Agora lista os clientes
    response = client.get(
        "/cliente_auth",  # ajuste conforme o prefixo real do seu router
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(cliente["nome"] == "Maria" for cliente in data)



@pytest.fixture
def token_valido():
    # Registra um usuário
    usuario = {"username": "admin1", "password": "1234"}
    client.post("/registro", json=usuario)

    # Faz login e pega o token
    response = client.post("/login", json=usuario)
    data = response.json()
    return data["access_token"]

def test_criar_cliente(token_valido):
    novo_cliente = {
        "nome": "João da Silva",
        "idade": 55
    }
    response = client.post(
        "/cliente_auth",  # rota de criação de cliente
        json=novo_cliente,
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert response.status_code == 200 or response.status_code == 201
    data = response.json()
    assert data["nome"] == "João da Silva"
    assert data["idade"] == 55

'''

import pytest
from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)

'''
pytest -s -v tests/test_postget_cliente.py

'''

@pytest.fixture
def token_valido():
    # Registra um usuário
    usuario = {"username": "admin1", "password": "1234"}
    client.post("/registro", json=usuario)
    # Faz login e pega o token
    response = client.post("/login", json=usuario)
    data = response.json()
    return data["access_token"]


def test_listar_clientes_formatado(token_valido):
    response = client.get(
        "/cliente_auth/",
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

    # Saída formatada em JSON bonito
    print("=== Lista de Clientes ===")
    print(json.dumps(data, indent=4, ensure_ascii=False))

    # Também pode mostrar só os nomes em formato de lista
    nomes = [cliente["nome"] for cliente in data]
    print("=== Nomes dos Clientes ===")
    for nome in nomes:
        print(f"- {nome}")


'''
def test_listar_clientes_sem_criar(token_valido):
    response = client.get(
        "/cliente_auth/",
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # Não exige lista vazia, apenas confirma que é uma lista
    assert all("nome" in cliente for cliente in data)


def test_listar_clientes_sem_criar(token_valido):
    response = client.get(
        "/cliente_auth/",
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

    # Mostra os nomes dos clientes retornados
    nomes = [cliente["nome"] for cliente in data]
    print("Clientes retornados:", nomes)

    # Se quiser apenas garantir que é uma lista, sem exigir vazia:
    assert all("nome" in cliente for cliente in data)



def test_listar_clientes(token_valido):
    
    # Cria um cliente para garantir que a lista não esteja vazia
    novo_cliente = {"nome": "Maria", "idade": 30}
    client.post(
        "/cliente_auth",  # ajuste conforme o prefixo real do seu router
        json=novo_cliente,
        headers={"Authorization": f"Bearer {token_valido}"}
    )

    # Agora lista os clientes
    response = client.get(
        "/cliente_auth",  # ajuste conforme o prefixo real do seu router
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(cliente["nome"] == "joao" for cliente in data)
'''