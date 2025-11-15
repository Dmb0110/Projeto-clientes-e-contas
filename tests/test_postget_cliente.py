
'''
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

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

