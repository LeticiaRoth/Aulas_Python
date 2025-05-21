import math

quantidade_numeros = int(input("Digite a quantidade de números que deseja multiplicar: "))
numeros = []

for i in range(quantidade_numeros):
    numero = float(input(f"Digite o número {i + 1}"))
    numeros.append(numero)

multiplicacao = math.prod(numeros)
print(f"A multiplicação dos números é igual a: {multiplicacao}")

"""
Posso utilizar o math.prod, ou utilizar o método abaixo:
multiplicacao = 0
for numero in numeros:
    multiplicacao += numero
"""