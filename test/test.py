from fastapi.testclient import TestClient
from src.main import *

import pytest
import pytest_asyncio

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Bem-vindo!"}

def test_adicionar():
    response = client.get("/adicionar?x=10&y=5")
    assert response.status_code == 200
    assert response.json() == {"resultado": 15}

def test_subtrair():
    response = client.get("/subtrair?x=10&y=5")
    assert response.status_code == 200
    assert response.json() == {"resultado": 5}

def test_multiplicar():
    response = client.get("/multiplicar?x=10&y=5")
    assert response.status_code == 200
    assert response.json() == {"resultado": 50}

def test_dividir():
    response = client.get("/dividir?x=10&y=5")
    assert response.status_code == 200
    assert response.json() == {"resultado": 2.0}

def test_dividir_zero():
    response = client.get("/dividir?x=10&y=0")
    assert response.status_code == 200
    assert response.text == '"Erro: divisão por zero!"\n'
