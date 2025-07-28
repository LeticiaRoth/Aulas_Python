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

"""


