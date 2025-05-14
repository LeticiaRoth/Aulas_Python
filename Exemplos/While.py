"""
#Se tirar o false, via ficar rodando infinitamente
x = True
while x:
    print("Estou rodando")
    x = False

#Vai de 1 a 5, enquanto o número for menor que 5
i = 1
while i <= 5:
    print(i)
    i += 1

#Enquanto não digitar, não irá sair
pedido = ''

while pedido != 'quero sair':
    pedido = input("Você não vai sair")


#Contador, com while e condição de break e continue
contador = 0

while contador < 9:
    print(contador, end=' ')
    contador += 1
    if contador == 5:
        continue #Mesmo se for 5 irá continuar rodando
        break #Colocando o break ele para no 4, pois começa no 0
"""