n = int(input("Digite a quantidade de múltiplos:"))
lista = []

for i in range(1, n +1):
    multiplo = 5 * i #Pega todos os números que são múltiplos de 5
    lista.append(multiplo)

print(f"Os {n} primeiros múltiplos de 5 são {lista}")