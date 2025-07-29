def criacaoDicionario(**kwargs):
    return kwargs

cliente1 = criacaoDicionario(nome="Letícia" , idade=18, valor_compra="R$40,00")
cliente2 = criacaoDicionario(nome="Claúdia" , idade=29, valor_compra="R$25,00")
cliente3 = criacaoDicionario(nome="Marcelo" , idade=78, valor_compra="R$99,00")

print(cliente1)
print(cliente2)
print(cliente3)