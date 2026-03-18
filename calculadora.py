# Calculadora inicial basica usando python
import os
os.system("cls")
print("Seja bem vindo a Calculadora Basica!")
print("Com esse programa você pode calcular rapidamente operações que desejar.")
enter = ""

operacoes = "*-+/"

while True:
    tecla = input("Pressione enter: ")
    
    if tecla == enter:
        try:
            num1 = int(input("Para começar, digite um numéro: "))
            opcao = input("Escolha uma operação: " \
            "[*]multiplicação [/]divisão [+]soma [-]subtração: ")
            num2 = int(input("Digite outro numéro: "))
        except ValueError:
            print("Por favor, digite um número inteiro")
            print("Exemplo: 1,2,3,5,10,20,30 e etc")
            continue

        try:
            if opcao == "*":
                os.system("cls")
                print(f"O resultado de {num1}*{num2} é igual a: {num1*num2}")
            elif opcao == "+":
                os.system("cls")
                print(f"O resultado de {num1}+{num2} é igual a: {num1+num2}")
        
            elif opcao == "/":
                os.system("cls")
                print(f"O resultado de {num1}/{num2} é igual a: {num1/num2}")
            elif opcao == "-":
                os.system("cls")
                print(f"O resultado de {num1}-{num2} é igual a: {num1-num2}")
            else:
                print(f"Por favor, apenas as operações: {operacoes}")

        except ZeroDivisionError:
            print("Impossivel dividir por 0")
            continue

        sair = input("Você quer sair? [s]sim [n]não: ")
        
        if sair == "s":
            print("Você saiu")
            break
        elif sair == "n":
            continue
        else:
            print("Por favor, digite [s] ou [n]: ")
    else:
        print("Por favor, tecle Enter.")
        continue
# Primeiro projeto feito sozinho por mim.
