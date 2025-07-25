def somar(y,x):
    return y + x

def subtrair(y,x):
    return  y - x

def multiplicacao(y,x):
    return y * x

def dividir (y,x):
    return y / x


def mostrar_menu():
    print("*** CALCULADORA SIMPLES ***")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")


while True:

    #Primeiro peço para o usuário colocar os numeros
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundo número:"))

    #Puxo a def que crie para mostrar o menu
    mostrar_menu()
    escolha = input("Escolha uma das opções acima:")

    if escolha == "1":
        #Crie uma função para cada então puxo elas
        print("Resultado da soma:", somar(n1,n2))
        break

    elif escolha == "2":
        print("Resultado de subtração", subtrair(n1,n2))
        break

    elif escolha == "3":
        print("Resultadp de multiplicação", multiplicacao(n1,n2))
        break

    elif escolha == "4":
        print("Resultado da divisão", dividir(n1,n2))
        break

    elif escolha == "5":
        print("Encerrando, volte sempre!")

    else:
        print("Opção inválida!")
        break










