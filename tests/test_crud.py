

import json
from fastapi.testclient import TestClient
from app.main import app

'''
COMANDOS PRA TESTAR COM PYTEST
pytest tests/test_crud.py
pytest -s -v tests/test_crud.py
pytest

pytest -s -v tests/test_registro.py

'''
client = TestClient(app)
'''
# Teste POST (criar recurso)
def test_criar_cliente():
    novo_cliente = {"nome": "João clemente", "idade": "20"}
    response = client.post("/cliente", json=novo_cliente)
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "João clemente"
    assert "id" in data

# Teste GET (listar recurso)
def test_listar_clientes():
    response = client.get("/cliente")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
'''
# Teste GET (listar todos e imprimir todos)
def test_get():
    response = client.get("/cliente")
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
    cliente_atualizado = {"nome": "João Silva", "idade": "29"}
    response = client.put("/cliente/10", json=cliente_atualizado)
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "João Silva"


# Teste DELETE (remover recurso)
def test_deletar_cliente():
    response = client.delete("/cliente/8")
    assert response.status_code == 200
    data = response.json()
    assert data["mensagem"] == "Cliente deletado com sucesso"

'''
