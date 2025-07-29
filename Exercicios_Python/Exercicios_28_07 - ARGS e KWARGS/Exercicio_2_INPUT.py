def criacaoDicionario(**kwargs):
    return kwargs

def exibir_formatado(cliente, numero):
    print(f"\nCliente {numero}:")
    for chave, valor in cliente.items():
        print(f"{chave}: {valor}")

#Salva os clientes dentro de uma lista
clientes = []

#Aparece no começo para dar um norte
print("Cadastro de clientes (digite 'sair' no nome para encerrar):")

#Vai comando mais um
contador = 1

while True:
    nome = input(f"\nDigite o nome do cliente {contador}: ")

    #Opção para sair do while, coloco o break com o sair
    if nome.lower() == "sair":
        break

    idade = input("Digite a idade: ")
    valor_compra = input("Digite o valor da compra (ex: R$40,00): ")

    cliente = criacaoDicionario(nome=nome, idade=idade, valor_compra=valor_compra)
    clientes.append(cliente)
    contador += 1


# Exibir todos os clientes formatados
for i, cliente in enumerate(clientes, start=1):
    exibir_formatado(cliente, i)
