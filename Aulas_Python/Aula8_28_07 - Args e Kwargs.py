"""
-> São usados para passar parâmetros muito grandes, uma variável de argumentos
para uma função.

- Uma túpla que permite passar um número variável de argumentos
posicionais para uma função, feita entre parenteses;



-----------------------------------
- ARGS = usado para passar argumentos posicionais (sem nome)
def minhaFuncao (*args):
    for arg in args:
        print(arg)

minhaFuncao(1,2,3)
-----------------
SEM ARGS ficaria assim:
def minhaFuncao(a, b, c):
    print(a)
    print(b)
    print(c)

COM ARGS fica assim:
def minhaFuncao(*args):
    for arg in args:
        print(arg)
minhaFuncao(1, 2, 3)

------------------------------------




-KWARGS - é usado para passar argumentos nomeados (com nome ou palavra-chave).
é um dicionario que permite passar um número, ele coleta todos os argumentos nomeados (com nome=valor) e transforma em um dicionário.

def minhaFuncao (**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

minhaFuncao(nome='Leticia', idade=18, cidade='Hortolândia')

-----------------------------------------

SEM KWARGS ficaria assim:
kwargs = {
    'nome': 'Leticia',
    'idade': 18,
    'cidade': 'Hortolândia'
}



COM KWARGS fica assim:
minhaFuncao(nome='Leticia', idade=18, cidade='Hortolândia')

-----------------------------------------------
EXEMPLOS

EX 1 - Interações
def media(num1,num2, *args):
    print(args)
    print(sum(args)/len(args))

media(1,5,6,7,8)
#Peguei o tamanho da tupla, divide pela soma dela, posso fazer interações com ela




EX 2 - Colocando o asterisco para reconhecer o args e indicar a tupla
notas = [3,6,8,9,9.96,4.2,]

def somarNotas(*args):
    print(args)
    print(sum(args))

#São varios dados em um, então coloco o asterisco e referencia o args
somarNotas(*notas)



EX 3 - Utilizando o kwargs
def idade(**kwargs):
    print(kwargs)
    for nome, idade in kwargs.items():
        print(f"Idade de {nome} é {idade}")

idade(maria=5, lucas=9, jessica=8)



EX 4 - Utilizando o for e o if
def jogadas(nome, **kwargs):
    print(kwargs)
    for jogada in kwargs:
        print(kwargs[jogada])
        if kwargs[jogada] == 10:
            return f"{nome} ganhou!"
    return f"{nome} perdeu!"

print(jogadas('Marcelo', j1=9,j2=8,j8=10,j4=9,j5=6))




EX 5 - Passando parametros
def apresentarNotas(joao,carlos,jessica):
    print(f'João: {joao}, Carlos:{carlos}, Jessica:{jessica}')

notas = {'joao': 7, 'carlos': 10, 'jessica': 9}
apresentarNotas(**notas)

"""
