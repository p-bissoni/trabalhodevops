# calculadora.py
from fastapi import FastAPI

app = FastAPI()

# Mensagem de boas-vindas
@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo!"}

# Realiza adição de dois números
@app.get("/adicionar")
def adicionar(x: float, y: float):
    return {"resultado": x + y}

# Realiza subtração de dois números
@app.get("/subtrair")
def subtrair(x: float, y: float):
    return {"resultado": x - y}

# Realiza multiplicação de dois números
@app.get("/multiplicar")
def multiplicar(x: float, y: float):
    return {"resultado": x * y}

#Realiza divisão de dois números, se o divisor for zero, retorna um mensagem de erro
@app.get("/dividir")
def dividir(x: float, y: float):
    if y == 0:
        return "Erro: divisão por zero!"
    return {"resultado": x / y}
