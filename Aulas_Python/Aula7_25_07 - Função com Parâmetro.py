"""
DEFINIÇÃO: Funções com parâmetro, rece um ou mais valores argumentos como entrada;

EX 1:
def saudacao(nome):
    print9("Olá, + nome)
saudacao("Maria")

-> Passo o parâmetro, muito utilizada quando o valor varia,
    sempre pode mudar, como em uma calculadora.

-----------------------------------------

EX 2:
def imparPar(numero):
    if numero % 2 == 0:
        print("Número par")
    else:
        print("Número não é par")

imparPar(20)
imparPar(89)

->Sem parâmetro dara erro, com o tipo;

------------------------------------------------
EX 3:
def separar (lista):
    for item in lista:
        if item > 10:
            print(item, end= '')

listaCriada = [12, 34, 90, 434, 89]
separar(listaCriada)

EX 4:
def cidade(parte1, parte2):
    print(parte1 + '' + parte2)

cidade('São', 'Paulo')
cidade('São', 'Paulo')

cidade(parte2='São', parte1='Paulo')

-----------------------------------------------

EX 5:
def medida(numero, referencia=60):
     if numero > referencia:
        print(f"{numero} é maior que {referencia}")
    else:
        print(f"{referencia} é maior que {numero}")

#Vai mostrar os icones em azul, mostrando o valor dos parâmetros, no caso numero e referencia
medida(40, 30)
"""