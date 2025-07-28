def Sequenciafibonacci(n):
    # Se N for 0 ou 1 retorna 0 ou 1.
    if n <= 1:
        return n
    #Calcular os dois números anteriores e somar eles.
    else:
        return Sequenciafibonacci(n - 1) + Sequenciafibonacci(n - 2)

lista_termos = []

def Gerarlista(n, lista_termos, indice=0):
    # Verificar se todos os termos já foram
    if indice == n:
        print(lista_termos)
        return

    # Chama a função para calcular o próximo termo e armazena na lista.
    lista_termos.append(Sequenciafibonacci(indice))

    Gerarlista(n, lista_termos, indice + 1)

n = int(input("Digite o número de termos da sequência Fibonacci: "))

Gerarlista(n, lista_termos)