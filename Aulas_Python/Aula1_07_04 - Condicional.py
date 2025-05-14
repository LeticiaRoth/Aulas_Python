
'''                         AULA 1 - 07/04/2025
# Programa Retãngulo
import math
base = float(input("Digite o valor da base:"))
altura = float(input("Digite a altura:"))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt( base ** 2 + altura ** 2)


print(f"Área: {area:.4f} Perimetro: {perimetro:.4f} Diagonal: {diagonal:4f}")




# Programa Idades
#Pessoa 1
nome_pessoa1 = input("Digite seu nome:")
idade_pessoa1 = int(input("Digite sua idade:"))


#Pessoa 2
nome_pessoa2 = input("\nDigite seu nome:")
idade_pessoa2 = float(input("Digite sua idade:"))

media = (idade_pessoa1 + idade_pessoa2) / 2

print(f"\nNome Pessoa 1:{nome_pessoa1} \nNome Pessoa 2: {nome_pessoa2}  \nMédia das idades:{media:.1f}")




# Programa Soma
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

soma = num1 + num2
print(f"Resultado: {soma}")




# Programa Troco
preco_unidade = float(input("Digite o preço da unidade:"))
quantidade_produtos = int(input("Digite a quantidade de produtos:"))
dinheiro_cliente = float(input("Dinheiro dado pelo cliente:"))

conta = quantidade_produtos * preco_unidade
troco = dinheiro_cliente - conta

print(f"Troco: {troco}")
'''