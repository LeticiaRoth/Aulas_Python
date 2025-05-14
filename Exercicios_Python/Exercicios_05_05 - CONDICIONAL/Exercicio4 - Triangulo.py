lado1 = float(input("Digite a medida do primeiro lado:"))
lado2 = float(input("Digite a medida do segundo lado:"))
lado3 = float(input("Digite a medidade do terceiro lado:"))

if lado1 == lado2 == lado3:
    print("Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
    print("Isósceles")
else:
    print("Escaleno")