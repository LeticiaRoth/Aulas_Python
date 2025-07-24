"""                 AULA 3 - 14/05/2025

LOOP - é  algo que se repete várias vezes (FOR)
for elemento in conjunto = como deve ser colocado

i = interação (usado como um contador, na maioria dos casos)


-------------------------------------------------------------------------------------
                      RANGE
Função que cria um intervalo de número escolhidps
range(número que você deseja que comece, numero que voce deseja que finalize + 1)
numero = range(2,10, -3) - o -3 vai pulando de três em três números


EXEMPLO:
invervalo_num = range(3,11) --- Quando chegar no 11, ele para, 11 é o comando de parada
for numero in invervalo_num:
    print(numero) - Começa do 3 e vai até o 10


------------------------------------------------------------------------------------
                      BREAK
-> Utilizando o break, que para o código, podendo colocar uma condição
string = 'Leticia'
for letra in string:
    print(letra, end='/')
    if letra == 't':
        break

seriado = 'Todo mundo odeia o Cris'
for letra in seriado:
    print(letra, end='.') - Vai printar cada letra com pontos



numero = [1, 2,'oi', True]
fro elemento in numero:
    print(elemento,end='.')- Vai printar cada letra com pontos

-----------------------------------------------------------------------------------

                       LISTA.APPEND()
EXEMPLO: para adicionar um item em uma lista vazio

numeros = [2,3,4,5]
lista = []
lista.append(numeros)

Irá adicionar todos os números dentro da lista, para isso usamos o append

-------------------------------------------------------------------------------------
                       EXERCÍCIO NÚMERO PRIMO
numero = int(input("Digite um número"))
primo = True #Nesse caso criei uma variável primo, declarando como verdadeira

for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break

if primo:
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")

-------------------------------------------------------------------------------------

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
