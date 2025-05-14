numero = 1
pares = 0 #Contaremos os números pares

while pares < 5: #Roda até imprimir os 5 números pares
    if numero % 2 == 0: #Verifica se o número é par
        print(numero)
        pares += 1 #Se for par conta mais 1
    numero += 1