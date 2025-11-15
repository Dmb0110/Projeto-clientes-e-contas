

import json
from fastapi.testclient import TestClient
from app.main import app

'''
COMANDOS PRA TESTAR COM PYTEST
pytest tests/test_crud.py
pytest -s -v tests/test_crud_conta.py
pytest

pytest -s -v tests/test_registro.py

'''
client = TestClient(app)


'''
# Teste POST (criar recurso)
def test_criar_cliente():
    novo_cliente = {"nome_do_banco": "", "numero_da_conta": "41","numero_da_agencia":""}
    response = client.post("/conta/conta", json=nova_conta)
    assert response.status_code == 201
    data = response.json()
    assert data["nome_do_banco"] == "hsbc"
    assert data["numero_da_conta"] == 2025
    assert data["numero_da_agencia"] == 22
    assert "id" in data

# Teste GET (listar recurso)
def test_listar_clientes():
    response = client.get("/cliente/cliente")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

'''
# Teste GET (listar todos e imprimir todos)
def test_get():
    response = client.get("/conta/conta")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data,list)
    assert len(data) > 0
    #assert response.json()[0]["nome_do_banco"] == "bradesco"
    print('\n Teste bem sucedido,dados retornados:')
    print(json.dumps(data,indent=2,ensure_ascii=False))

'''
# Teste PUT (atualizar recurso)
def test_atualizar_cliente():
    cliente_atualizado = {"nome": "euclides Silva", "idade": "41"}
    response = client.put("/cliente/cliente/20", json=cliente_atualizado)
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "euclides Silva"


# Teste DELETE (remover recurso)
def test_deletar_cliente():
    response = client.delete("/cliente/cliente/20")
    assert response.status_code == 200
    data = response.json()
    assert data["mensagem"] == "Cliente deletado com sucesso"

'''
