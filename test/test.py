from src.main import *
from unittest.mock import patch
from fastapi.testclient import TestClient
from fastapi import FastAPI, HTTPException

client = TestClient(app)

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

@app.get("/dividir")
def test_dividir(x: int, y: int):
    if y == 0:
        raise HTTPException(status_code=400, detail="Erro: divisão por zero!")
    return {"resultado": x / y}

def test_dividir_zero():
    response = client.get("/dividir?x=10&y=0")
    assert response.status_code == 400 
    assert response.json() == {"detail": "Erro: divisão por zero!"}