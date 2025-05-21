lista_preco = []
lista_produtos = []

for i in range(1,6): #Determina a quantidade
    produto = input(f"Digite o {i} produto:")
    produtos = produto.title()

    if produto.isalpha():
        lista_produtos.append(produtos)
    else:
        print("Atenção: deve ser inserido o nome do produto")

    preco = float(input(f"Digite o preço do {i} produto: R$"))
    lista_preco.append(preco)

    print("\n")


soma_preco = sum(lista_preco)
print(f"Seu carrinho:{lista_produtos}")
print(f"Total da compra: R${soma_preco:.2f}")
