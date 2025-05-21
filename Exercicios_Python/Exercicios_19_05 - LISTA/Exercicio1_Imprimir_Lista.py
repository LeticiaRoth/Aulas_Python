quantidade_nomes = int(input("Quantos nomes deseja inserir? "))
nomes = []

for i in range(quantidade_nomes):
    nome = input(f"Digite o nome {i + 1}: ")
    nomes.append(nome)

print("\nNomes digitados:")
for nome in nomes:
    print(nome)