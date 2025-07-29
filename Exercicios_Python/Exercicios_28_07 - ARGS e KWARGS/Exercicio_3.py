def concatenaArgumentos(*args, **kwargs):
    resultado = ""

    # Concatena todos os argumentos posicionais (ARGS)
    for arg in args:
        resultado += str(arg) +" "

    # Concatena todos os valores dos argumentos nomeados (KWARGS)
    for valor in kwargs.values():
        resultado += str(valor) + " "

    return resultado

resultado = concatenaArgumentos("Olá, ", "mundo! ", nome="Letícia" ,idade=18, curso="DS")
print(resultado)
