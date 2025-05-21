quantidade_numeros = int(input("Insira quantos números deseja somar: "))
numeros = []

for i in range(quantidade_numeros):
    numero = float(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

soma = sum(numeros)
print(f"A soma dos números é igual a: {soma}")