numero = int(input("Digite um número:"))
lista_divisor = []

for i in range(1, numero + 1):
    if numero % i == 0:
        lista_divisor.append(i)

print(f"\nOs divisores são: {lista_divisor}")

soma = sum(lista_divisor)
print(f"Soma dos divisores: {soma}")
