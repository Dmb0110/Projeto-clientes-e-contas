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

def test_criar_conta(token_valido):
    nova_conta = {
        "nome_do_banco": "caixa",
        "numero_da_agencia": 2025,
        "numero_da_conta": 21,
        "cliente_id":7
    }
    response = client.post(
        "/conta_auth",  # rota de criação de cliente
        json=nova_conta,
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert response.status_code == 200 or response.status_code == 201
    data = response.json()
    assert data["nome_do_banco"] == "caixa"
    assert data["numero_da_agencia"] == 2025
    assert data['numero_da_conta'] == 21
    assert data['cliente_id'] == 7

'''


import pytest
from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)
'''
pytest -s -v tests/test_postget_conta.py
'''

@pytest.fixture
def token_valido():
    usuario = {"username": "admin1", "password": "1234"}
    client.post("/registro", json=usuario)
    response = client.post("/login", json=usuario)
    data = response.json()
    return data["access_token"]

def test_listar_contas(token_valido):
    response = client.get(
        "/conta_auth/",
        headers={"Authorization": f"Bearer {token_valido}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

# Exibir todos os campos de cada conta em formato de tabela
    print("\n=== Contas (Banco | Agência | Conta | Cliente) ===")
    for conta in data:
        print(
            f"{conta['nome_do_banco']} | "
            f"{conta['numero_da_agencia']} | "
            f"{conta['numero_da_conta']} | "
            f"{conta['cliente_id']}"
        )

    # Também pode mostrar só os nomes dos bancos
    nomes = [conta["nome_do_banco"] for conta in data]
    print("\n=== Lista das Contas ===")
    for nome in nomes:
        print(f"- {nome}")

