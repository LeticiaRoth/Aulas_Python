nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

media = (nota1 + nota2) / 2

if media == 5 and media <= 6:
    print("Recuperação")
elif media >= 7 and media <=10:
    print("Aprovado")
else:
    print("Reprovado")