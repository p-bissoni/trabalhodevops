# calculadora.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo!"}

@app.get("/adicionar")
def adicionar(x: float, y: float):
    return {"resultado": x + y}

@app.get("/subtrair")
def subtrair(x: float, y: float):
    return {"resultado": x - y}

@app.get("/multiplicar")
def multiplicar(x: float, y: float):
    return {"resultado": x * y}

@app.get("/dividir")
def dividir(x: float, y: float):
    if y == 0:
        return "Erro: divisão por zero!"
    return {"resultado": x / y}