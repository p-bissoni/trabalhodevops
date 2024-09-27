# calculadora.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    # Mensagem de boas-vindas
    return {"mensagem": "Bem-vindo!"}

@app.get("/adicionar")
def adicionar(x: float, y: float):
    # Realiza adição de dois números
    return {"resultado": x + y}

@app.get("/subtrair")
def subtrair(x: float, y: float):
    # Realiza subtração de dois números
    return {"resultado": x - y}

@app.get("/multiplicar")
def multiplicar(x: float, y: float):
    # Realiza multiplicação de dois números
    return {"resultado": x * y}

@app.get("/dividir")
def dividir(x: float, y: float):
    #Realiza divisão de dois números, se o divisor for zero, retorna um mensagem de erro
    if y == 0:
        return "Erro: divisão por zero!"
    return {"resultado": x / y}