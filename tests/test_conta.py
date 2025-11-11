'''
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_listar_clientes():
    response = client.get("/conta")
    assert response.status_code == 200
    print('teste realizado com sucesso')


import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_listar_clientes():
    response = client.get("/conta")
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
    response = client.get("/conta")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data,list)
    assert len(data) > 0
    #assert response.json()[0]["nome_do_banco"] == "bradesco"
    print('\n Teste bem sucedido,dados retornados:',data)
'''
