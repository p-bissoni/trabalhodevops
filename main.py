# calculadora.py

# Adicionar dois números
def adicionar(x, y):
    return x + y

# Subtrair dois números
def subtrair(x, y):
    return x - y

# Multiplicar dois números
def multiplicar(x, y):
    return x * y

# Dividir dois números
def dividir(x, y):
    if y == 0:
        return "Erro: divisão por zero!"
    return x / y

# Menu da calculadora
def menu():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

# Programa principal
while True:
    menu()
    
    # Recebe a entrada do usuário
    escolha = input("Digite sua escolha (1/2/3/4) ou 'sair' para encerrar: ")

    if escolha == 'sair':
        print("Fechando a Calculadora.")
        break

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"{num1} + {num2} = {adicionar(num1, num2)}")

        elif escolha == '2':
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")

        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

        elif escolha == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")

    else:
        print("Escolha inválida. Tente novamente.")

