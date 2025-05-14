idade = int(input("Digite sua idade:"))

if idade < 12:
    print("Criança")

elif idade >= 12 and idade <= 17:
    print("Adolescente")

elif idade >= 18 and idade <=29:
    print("Jovem")

elif idade >= 30 and idade <= 65:
    print("Adulto")
else:
    print("Idoso")